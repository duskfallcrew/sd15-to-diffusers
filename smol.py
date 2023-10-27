import requests
import os
import re
import datetime
import shutil
import convert_vae

from diffusers.pipelines.stable_diffusion.convert_from_ckpt import download_from_original_stable_diffusion_ckpt

min_name_length = 6

params = {
    'limit' : '1',
    'types': 'Checkpoint',
    'sort': 'Most Downloaded',
    'period': 'Week',
}

response = requests.get('https://civitai.com/api/v1/models', params=params).json()

for model in response['items']:
    inpaint = False
    for i, item in enumerate(model['modelVersions']):
        #Checks for inpainting     
        if inpaint:
            break
        if 'inpaint' in item['name'].lower():
            inpaint = True
        elif i:
            continue

#Skips duplicate ids
        ID = str(item['id'])
        found = False
        with open('ids.txt', 'r') as f: lines = f.readlines()
        for line in reversed(lines): 
            if ID == line: 
                found = True 
                break  
        if found: 
            continue
            
        #Investigates model
        config = False
        vae = False
        ID = str(item['id'])
        info = requests.get('https://civitai.com/api/v1/model-versions/' + ID).json()
        if '2' in info['baseModel']:
            continue
        if len(info['trainedWords']) == 1:
            trigger_word = info['trainedWords']
        for file in info['files']:
            url = file['downloadUrl']
            if not config and file['type'] == 'Config': 
                config = True
                with open('config.yaml', 'wb') as f: f.write(requests.get(url).content) 
            elif not vae and file['type'] == 'VAE':
                vae = True
                with open('vae.pt', 'wb') as f: f.write(requests.get(url).content) 
            elif file['primary'] == True:
                filename = file['name'].strip('"')
                with open(filename, 'wb') as f: f.write(requests.get(url).content)
                
        #Filters name
        name = re.sub('[^-()[\]_\s\'a-z\d]', '', model['name'].lower())
        name = re.findall('[^-()[\]_\s]+', name)
        if "'" not in name[0] and len(name[0]) >= min_name_length or len(name) < 2:
            name = name[0]
        elif "'" in name[0] and len(name[1]) >= min_name_length:
            name = name[1]
        else:
            if "'" in name[0] and len(name[1]) < min_name_length and len(name) > 2:
                del name[0]
            name = name[0]+'-'+name[1] 
        name = name.strip("'")
        if not re.search('[a-z]', name) or len(name) < min_name_length: 
            name = 'Placeholder'
        
        #Indexes name
        with open('names.txt', 'r') as f: lines = f.readlines()  
        index = 0
        name += '-inpainting' if inpaint and 'inpaint' not in name else '' 
        for line in reversed(lines):
            if line.startswith(name):
                if line == name:
                    index = max(1,index)
                elif line[len(name)] == '-' and line[len(name)+1:].isnumeric(): 
                    index = max(int(line.split('-')[1]),index)
        name += '-' + str(index+1) if index else ''
        
        #Converts model
        try:
            model_path = './' + filename
            pipe = download_from_original_stable_diffusion_ckpt(
                model_path,
                './config.yaml' if config else None,
                from_safetensors=True if filename.endswith('safetensors') else False 
            )
            diffuser_path = './' + name
            pipe.save_pretrained(diffuser_path) 
            if vae:
                shutil.rmtree(diffuser_path + '/vae')
                convert_vae.vae_pt_to_vae_diffuser('./vae.pt', diffuser_path + '/vae')             
        except:
            continue
        finally:
            os.remove(model_path)
            if config: os.remove('./config.yaml')
            if vae: os.remove('./vae.pt')                              
      
        #Appends data to txt files
        with open('ids.txt', 'a') as f: f.write(ID + '\n') 
        with open('names.txt', 'a', encoding='utf-8') as f: f.write(model['name'] + '\n')
        with open('new_names.txt', 'a') as f: f.write(name + '\n')