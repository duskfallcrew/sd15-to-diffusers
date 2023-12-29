# -*- coding: utf-8 -*-
"""Converter_SD1_5_V3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zAzdsaa2KQcF6W0V4eCLZ6eUO8hsDJTo

# **SD 1.5 Model Converter**

 **A Colab Notebook To Convert SD 1.5 Checkpoint to Diffusers format**

But a horribly duct taped edition. THIS IS IN ALPHA STAGES, WILL BE PATCHING THE CODE AS I GO ALONG.

---
Link to this colab: https://colab.research.google.com/github/duskfallcrew/sd15-to-diffusers/blob/main/Converter_SD1_5_V2_FIXED.ipynb

***Patched from*** : https://colab.research.google.com/github/Linaqruf/sdxl-model-converter/blob/main/sdxl_model_converter.ipynb


RIGHT NOW THE INSTRUCTIONS ARE AS FOLLOWS:

♻ - Install/Clone etc

♻ - Download model - Direct port from Linaqruf.

♻ - Put your model details in.

♻ - DUMP PATH = folder name

♻ - If your downloaded model is safetensors please tick the box.

♻ - Check file browser, if the model/yourmodelhere looks like a diffusers format you're good to go!

♻ - Write Token + Set up your Repo!

♻ - Upload Diffusers!


---

Ahoy! you're looking for our Huggingface backup that is again patched from Linaqruf and others?

| Notebook Name | Description | Link |
| --- | --- | --- |
| [Huggingface Backup](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb) | backup checkpoints! | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb)

---

## Duskfall/ Earth & Dusk Socials

Discord:
![Discord](https://img.shields.io/discord/1024442483750490222?label=Earth%26Dusk&style=plastic)

---

| Social Network |  Link |
| --- |  --- |
|Discord|[Invite](https://discord.gg/5t2kYxt7An)
|CivitAi|[Duskfallcrew](https://civitai.com/user/duskfallcrew/)
|Huggingface|[Earth & Dusk](https://huggingface.co/EarthnDusk)
|Ko-Fi| [Dusk's Kofi](https://ko-fi.com/duskfallcrew/)

---

***Linaqruf @ Github***: https://github.com/Linaqruf

 [![](https://dcbadge.vercel.app/api/shield/850007095775723532?style=flat)](https://lookup.guru/850007095775723532) [![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/linaqruf) <a href="https://saweria.co/linaqruf"><img alt="Saweria" src="https://img.shields.io/badge/Saweria-7B3F00?style=flat&logo=ko-fi&logoColor=white"/></a>

---

 **Please use their main scripts for SDXL HERE:**

| Notebook Name | Description | Link |
| --- | --- | --- |
| [Kohya LoRA Trainer XL](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-trainer-XL.ipynb) | LoRA Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-trainer-XL.ipynb) |
| [Kohya Trainer XL](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-trainer-XL.ipynb) | Native Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-trainer-XL.ipynb) |

---
SD 1.5 Scripts:

| Notebook Name | Description | Link | V14 |
| --- | --- | --- | --- |
| [Kohya LoRA Dreambooth](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-dreambooth.ipynb) | LoRA Training (Dreambooth method) | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-dreambooth.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-LoRA-dreambooth.ipynb) |
| [Kohya LoRA Fine-Tuning](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-finetuner.ipynb) | LoRA Training (Fine-tune method) | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-finetuner.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-LoRA-finetuner.ipynb) |
| [Kohya Trainer](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-trainer.ipynb) | Native Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-trainer.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-trainer.ipynb) |
| [Kohya Dreambooth](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-dreambooth.ipynb) | Dreambooth Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-dreambooth.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-dreambooth.ipynb) |

Disclaimer:
This doesn't run the inference like the SDXL one, we don't understand how to patch that.

IN THEORY This should work on anything that uses Jupyter, we'll test it later on via Vast or Runpod, and if you see this line edited eventually? You know it's working!

Duskfallcrew/Earth and Dusk take no responsibility for the horribly patched code. Nor likely does Linaqruf. Do not smack us, do not sue us, don't sue Linaqruf!

Updates:

Patched the conversion, added snarky comments to the outputs.
Our personal one has funny notes, feel free to patch and change at will.

Added a fix keys for models that won't convert, and also added a patch for cleaning folders.
"""

#@title ## ♻ **Install Diffusers**
import os
from subprocess import getoutput

!apt install aria2
!pip install diffusers
!pip install omegaconf
!pip install transformers
!pip install xformers
!pip install accelerate
!git clone https://github.com/huggingface/diffusers

# Directories
root_dir = "/content"
repo_dir = os.path.join(root_dir, "diffusers")
models_dir = os.path.join(root_dir, "models")
vae_dir = os.path.join(root_dir, "vae")

def prepare_environment():
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.environ["SAFETENSORS_FAST_GPU"] = "1"
    os.environ["PYTHONWARNINGS"] = "ignore"
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "garbage_collection_threshold:0.9,max_split_size_mb:512"
    os.environ["TCMALLOC_AGGRESSIVE_DECOMMIT"] = "t"
    os.environ["CUDA_MODULE_LOADING"] = "LAZY"

def main():
    os.chdir(root_dir)
    os.chdir(repo_dir)
    prepare_environment()

def main():
    print(f"♻ Deployment Complete, Head to downloading your model please.")

main()

# @title ## ♻ **Download SD 1.5**
import os
import re
import json
import glob
import gdown
import requests
import subprocess
from urllib.parse import urlparse, unquote
from pathlib import Path

os.chdir(root_dir)

# @markdown Place your Huggingface [Read Token](https://huggingface.co/settings/tokens) Here.

HUGGINGFACE_TOKEN = "yourreadtokengoeshere"#@param {type: "string"}
SD_MODEL_URL = "https whatever your model link is here" #@param {type: "string"}


def get_supported_extensions():
    return tuple([".ckpt", ".safetensors", ".pt", ".pth"])

def get_filename(url):
    extensions = get_supported_extensions()

    if url.endswith(tuple(extensions)):
        filename = os.path.basename(url)
    else:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        if 'content-disposition' in response.headers:
            content_disposition = response.headers['content-disposition']
            filename = re.findall('filename="?([^"]+)"?', content_disposition)[0]
        else:
            url_path = urlparse(url).path
            filename = unquote(os.path.basename(url_path))

    if filename.endswith(tuple(get_supported_extensions())):
        return filename
    else:
        return None

def parse_args(config):
    args = []

    for k, v in config.items():
        if k.startswith("_"):
            args.append(f"{v}")
        elif isinstance(v, str) and v is not None:
            args.append(f'--{k}={v}')
        elif isinstance(v, bool) and v:
            args.append(f"--{k}")
        elif isinstance(v, float) and not isinstance(v, bool):
            args.append(f"--{k}={v}")
        elif isinstance(v, int) and not isinstance(v, bool):
            args.append(f"--{k}={v}")

    return args

def aria2_download(dir, filename, url):
    user_header = f"Authorization: Bearer {HUGGINGFACE_TOKEN}"

    aria2_config = {
        "console-log-level"         : "error",
        "summary-interval"          : 10,
        "header"                    : user_header if "huggingface.co" in url else None,
        "continue"                  : True,
        "max-connection-per-server" : 16,
        "min-split-size"            : "1M",
        "split"                     : 16,
        "dir"                       : dir,
        "out"                       : filename,
        "_url"                      : url,
    }
    aria2_args = parse_args(aria2_config)
    subprocess.run(["aria2c", *aria2_args])

def gdown_download(url, dst, filepath):
    if "/uc?id/" in url or "/file/d/" in url:
        return gdown.download(url, filepath, quiet=False)
    elif "/drive/folders/" in url:
        os.chdir(dst)
        return gdown.download_folder(url, quiet=True, use_cookies=False)

def download(url, dst):
    filename = get_filename(url)
    filepath = os.path.join(dst, filename)

    if "drive.google.com" in url:
        gdown = gdown_download(url, dst, filepath)
    elif url.startswith("/content/drive/MyDrive/"):
        return url
    else:
        if "huggingface.co" in url:
            if "/blob/" in url:
                url = url.replace("/blob/", "/resolve/")
        aria2_download(dst, filename, url)

def main():
    model_path = SD_MODEL_URL
    vae_path = VAE_MODEL_URL
    download(model_path, models_dir)
    print(f"Model downloaded at: {model_path}")

def main():
    print(f"♻ Download complete, head to conversion.")

main()

# @title ## ♻ **Fix Before Converting**
from safetensors import safe_open
from safetensors.torch import save_file

def fix_diffusers_model_conversion(load_path: str = None, save_path: str = None):
    # Use default paths if not provided
    load_path = load_path or "input"  # @param {type: "string"}
    save_path = save_path or "output"  # @param {type: "string"}

    # load original
    tensors = {}
    with safe_open(load_path, framework="pt") as f:
        for key in f.keys():
            tensors[key] = f.get_tensor(key)

    # migrate
    new_tensors = {}
    for k, v in tensors.items():
        new_key = k
        # only fix the vae
        if 'first_stage_model.' in k:
            # migrate q, k, v keys
            new_key = new_key.replace('.to_q.weight', '.q.weight')
            new_key = new_key.replace('.to_q.bias', '.q.bias')
            new_key = new_key.replace('.to_k.weight', '.k.weight')
            new_key = new_key.replace('.to_k.bias', '.k.bias')
            new_key = new_key.replace('.to_v.weight', '.v.weight')
            new_key = new_key.replace('.to_v.bias', '.v.bias')
        new_tensors[new_key] = v

    # save
    save_file(new_tensors, save_path)

# Example usage
fix_diffusers_model_conversion(load_path='/content/drive/path/to/your/original_file.pth',
                               save_path='/content/drive/path/to/save/fixed_file.pth')

# @title ### ♻ **Clean Folders for Optimized Space**

from IPython.display import display, Markdown
import os
import shutil

# Function to clear and delete a folder
def clear_and_delete_folder(colab_folder_path):
    try:
        # Use shutil.rmtree to remove all files and subdirectories
        shutil.rmtree(colab_folder_path)
        display(Markdown(f"Deleted all contents in folder: `{colab_folder_path}`"))
    except Exception as e:
        display(Markdown(f"Error deleting folder `{colab_folder_path}`: {e}"))

# @markdown ### Folder Path for Deletion

colab_folder_path = "/content/models/yourinputhere" # @param {type: "string"}

# Call the function to clear and delete the folder
clear_and_delete_folder(colab_folder_path)

#@title ## ♻ **Convert SD 1.5 to Diffusers**

import os
import urllib.request
from urllib.parse import urlparse, unquote
from pathlib import Path



os.chdir(root_dir)
#@markdown ### **Conversion Config**
#@markdown Make sure you TICK SAFETENSORS or it won't convert.
#@markdown Dump path is where you would like your model to be stored before uploading.

checkpoint_path = "/models/modelname.safetensors" #@param {'type': 'string'}
dump_path = "/models/modelname" #@param {'type': 'string'}
from_safetensors = True  # @param {type: "boolean"}

def convert_dict(config):
    args = ""
    for k, v in config.items():
        if k.startswith("_"):
            args += f'"{v}" '
        elif isinstance(v, str):
            args += f'--{k}="{v}" '
        elif isinstance(v, bool) and v:
            args += f"--{k} "
        elif isinstance(v, float) and not isinstance(v, bool):
            args += f"--{k}={v} "
        elif isinstance(v, int) and not isinstance(v, bool):
            args += f"--{k}={v} "
    return args



def check_and_download_script(script_name, script_url):
    if not os.path.exists(script_name):
        print(f"{script_name} not found, downloading...")
        urllib.request.urlretrieve(script_url, script_name)

def run_script(script_name, script_args):
    !python {script_name} {script_args}


def main():
    script_name = "convert_original_stable_diffusion_to_diffusers.py"
    script_url = "https://raw.githubusercontent.com/huggingface/diffusers/main/scripts/convert_original_stable_diffusion_to_diffusers.py"
    check_and_download_script(script_name, script_url)

    config = {
        "checkpoint_path": checkpoint_path,
        "dump_path": dump_path,
        "from_safetensors": from_safetensors,

    }
    run_script(script_name, convert_dict(config))
    print(f"♻ Conversion Succesful, head to upload!")

main()

# @title ### ♻ **Huggingface Hub config**
from huggingface_hub import login, HfApi
from huggingface_hub.utils import validate_repo_id, HfHubHTTPError

# @markdown Login to Huggingface Hub
# @markdown > Get **your** huggingface `WRITE` token [here](https://huggingface.co/settings/tokens)
write_token = "yourtokengoeshere"  # @param {type:"string"}
# @markdown Fill this if you want to upload to your organization, or just leave it empty.
orgs_name = "yourorganizationisoptinalitgoeshere"  # @param{type:"string"}
# @markdown If your model repo does not exist, it will automatically create it.
model_name = "modelname"  # @param {type:"string"}
make_private = False  # @param{type:"boolean"}

def authenticate(write_token):
    login(write_token, add_to_git_credential=True)
    api = HfApi()
    return api.whoami(write_token), api

def create_model_repo(api, user, orgs_name, model_name, make_private=False):
    if orgs_name == "":
        repo_id = user["name"] + "/" + model_name.strip()
    else:
        repo_id = orgs_name + "/" + model_name.strip()

    try:
        validate_repo_id(repo_id)
        api.create_repo(repo_id=repo_id, repo_type="model", private=make_private)
        print(f"Model repo '{repo_id}' didn't exist, creating repo")
    except HfHubHTTPError as e:
        print(f"♻ Repository existed,  '{repo_id}' exists, skipping create repo, head to upload.")

    print(f"♻ Repository created, head to upload. Model repo '{repo_id}' link: https://huggingface.co/{repo_id}\n")

    return repo_id

user, api = authenticate(write_token)

if model_name:
    model_repo = create_model_repo(api, user, orgs_name, model_name, make_private)

# @title ### ♻ **Upload to Huggingface**
from huggingface_hub import HfApi
from pathlib import Path
import os

api = HfApi()

# @markdown This will be uploaded to model repo
model_path = "/content/models/yourinputhere"  # @param {type :"string"}
path_in_repo = ""  # @param {type :"string"}
project_name = os.path.basename(model_path)

# @markdown Other Information
commit_message = "Upload with \uD83D\uDE80\uD83E\uDD17 SD 1.5 Diffusers notebook"  # @param {type :"string"}

def is_diffusers_model(model_path):
    required_folders = {"unet", "text_encoder", "text_encoder_2", "tokenizer", "tokenizer_2", "scheduler", "vae"}
    return required_folders.issubset(set(os.listdir(model_path))) and os.path.isfile(os.path.join(model_path, "model_index.json"))

def upload_model(model_paths, is_folder: bool):
    path_obj = Path(model_paths)
    trained_model = path_obj.parts[-1]

    path_in_repo_local = path_in_repo if path_in_repo and not is_diffusers_model(model_paths) else ""

    notification = f"Uploading {trained_model} from {model_paths} to https://huggingface.co/{model_repo}"
    print(notification)

    if is_folder:
        if is_diffusers_model(model_paths):
            commit_message = f"Upload diffusers format: {trained_model}"
            print("Detected diffusers model. Adjusting upload parameters.")
        else:
            commit_message = f"Upload checkpoint: {trained_model}"
            print("Detected regular model. Adjusting upload parameters.")

        api.upload_folder(
            folder_path=model_paths,
            path_in_repo=path_in_repo_local,
            repo_id=model_repo,
            commit_message=commit_message,
            ignore_patterns=".ipynb_checkpoints",
        )
    else:
        commit_message = f"Upload file: {trained_model}"
        api.upload_file(
            path_or_fileobj=model_paths,
            path_in_repo=path_in_repo_local,
            repo_id=model_repo,
            commit_message=commit_message,
        )

    success_notification = f"♻ Model upload complete, care to try again? Thanks for flying Stable Diffusion Airlines, you owe me five dollars.. Check the model at https://huggingface.co/{model_repo}/tree/main"
    print(success_notification)

def upload():
    if model_path.endswith((".ckpt", ".safetensors", ".pt")):
        upload_model(model_path, False)
    else:
        upload_model(model_path, True)

upload()