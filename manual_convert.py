print('Importing Modules')

import requests
import convert_vae 
import shutil
import re
import os

from diffusers.pipelines.stable_diffusion.convert_from_ckpt import download_from_original_stable_diffusion_ckpt

print('Imported Modules')

while True: 

    url = input("URL: ")

    if 'modelVersionId' in url:
        model = requests.get('https://civitai.com/api/v1/model-versions/' + url.split('modelVersionId=')[1].split('?')[0]).json()
        model_name = model['model']['name'] 
    else:
        model = requests.get('https://civitai.com/api/v1/models/' + re.sub('[^\d]', '', url)).json()
        model_name = model['name']
        model = model['modelVersions'][0]   
        
    version_name = model['name']
    name = re.sub('[^-_\s\'a-z\d]', '', (model_name + ' ' + version_name).lower())
    folder_path = './downloads/' + name
    os.mkdir(folder_path)

    print('Model Name: ' + model_name)
    print('Version Name: ' + version_name)
    print('Made Directory: ' + name)
    
    config_path = './inpainting.yaml' if 'inpaint' in name or re.search('inp(?![a-z])', version_name) else False
    vae_path = False

    print('Inpainting: ' + ('True' if config_path else 'False')) 

    for file in model['files']:
        url = file['downloadUrl']
        if not config_path and file['type'] == 'Config': 
            print('Downloading Config')
            config_path = folder_path + '/config.yaml'
            with open(config_path, 'wb') as f: f.write(requests.get(url).content) 
            print('Downloaded Config')
        elif not vae_path and file['type'] == 'VAE':
            print('Downloading VAE')
            vae_path = folder_path + '/vae.pt'
            with open(vae_path, 'wb') as f: f.write(requests.get(url).content) 
            print('Downloaded VAE')
        elif file['primary'] == True:
            file_name = '/model.' + file['name'].split('.')[-1].strip('"')
            print('Safetensors: ' + ('True' if file_name.endswith('safetensors') else 'False'))
            print('Downloading Model')
            model_path = folder_path + file_name
            with open(model_path, 'wb') as f: f.write(requests.get(url).content)
            print('Downloaded Model')
                        
    pipe = download_from_original_stable_diffusion_ckpt(
        model_path,
        config_path if config_path else None,
        from_safetensors=True if file_name.endswith('safetensors') else False 
    )
    diffuser_path = './conversions/' + name
    pipe.save_pretrained(diffuser_path) 
    if vae_path:
        shutil.rmtree(diffuser_path + '/vae')
        convert_vae.vae_pt_to_vae_diffuser(vae_path, diffuser_path + '/vae') 
        
    print('Conversion Successful')    