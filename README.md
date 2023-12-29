
# **SD 1.5 Model Converter**

<a target="_blank" href="https://colab.research.google.com/github/duskfallcrew/sd15-to-diffusers/blob/main/Converter_SD1_5_V2_FIXED.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


 **A Colab Notebook To Convert SD 1.5 Checkpoint to Diffusers format**

But a horribly duct taped edition. THIS IS IN ALPHA STAGES, WILL BE PATCHING THE CODE AS I GO ALONG.

<a href="https://civitai.com/models/179789"> Check it out on Civitai here  </a> 

Updates:

Patched the conversion, added snarky comments to the outputs.
Our personal one has funny notes, feel free to patch and change at will.

Added a fix keys for models that won't convert, and also added a patch for cleaning folders.

Future ideas:

- Looking to port PT to safetensors into the same notebook.
- Looking to port inference for testing into the same notebook.
- Looking to figure out how to convert a different vae.
- Looking to figure out how to manage to get the conversions to roll on google drive for more space options.
- Porting it to VastAi/Runpod

If you're interested in tipping please hit me up: https://ko-fi.com/duskfallcrew

Also feel free to add your own code and rejig the notebook and upload your own version to your own repository, this is not going to be the first, it isn't the first - it's just since Camenduru's broke, we didn't have many options.  Yes, there's GUI for people to use NMKD i think uses a gui, but if you're on a Mac like me or don't have a decent GPU, this is a great option.


---




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



***Patched from*** : https://colab.research.google.com/github/Linaqruf/sdxl-model-converter/blob/main/sdxl_model_converter.ipynb

***Linaqruf @ Github***: https://github.com/Linaqruf

 [![](https://dcbadge.vercel.app/api/shield/850007095775723532?style=flat)](https://lookup.guru/850007095775723532) [![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/linaqruf) <a href="https://saweria.co/linaqruf"><img alt="Saweria" src="https://img.shields.io/badge/Saweria-7B3F00?style=flat&logo=ko-fi&logoColor=white"/></a>


 **Please use their main scripts for SDXL HERE:**

| Notebook Name | Description | Link |
| --- | --- | --- |
| [Kohya LoRA Trainer XL](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-trainer-XL.ipynb) | LoRA Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-trainer-XL.ipynb) |
| [Kohya Trainer XL](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-trainer-XL.ipynb) | Native Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-trainer-XL.ipynb) |

SD 1.5 Scripts:

| Notebook Name | Description | Link | V14 |
| --- | --- | --- | --- |
| [Kohya LoRA Dreambooth](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-dreambooth.ipynb) | LoRA Training (Dreambooth method) | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-dreambooth.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-LoRA-dreambooth.ipynb) |
| [Kohya LoRA Fine-Tuning](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-finetuner.ipynb) | LoRA Training (Fine-tune method) | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-finetuner.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-LoRA-finetuner.ipynb) |
| [Kohya Trainer](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-trainer.ipynb) | Native Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-trainer.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-trainer.ipynb) |
| [Kohya Dreambooth](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-dreambooth.ipynb) | Dreambooth Training | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/main/kohya-dreambooth.ipynb) | [![](https://img.shields.io/static/v1?message=Older%20Version&logo=googlecolab&labelColor=5c5c5c&color=e74c3c&label=%20&style=flat)](https://colab.research.google.com/github/Linaqruf/kohya-trainer/blob/ff701379c65380c967cd956e4e9e8f6349563878/kohya-dreambooth.ipynb) |


Ahoy! you're looking for our Huggingface backup that is again patched from Linaqruf and others?

| Notebook Name | Description | Link |
| --- | --- | --- |
| [Huggingface Backup](https://colab.research.google.com/github/duskfallcrew/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb) | backup checkpoints! | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/duskfallcrew/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb)

## Duskfall/ Earth & Dusk Socials
![Discord](https://img.shields.io/discord/1024442483750490222?label=Earth%26Dusk&style=plastic)

| Social Network |  Link |
| --- |  --- |
|Discord|[Invite](https://discord.gg/5t2kYxt7An)
|CivitAi|[Duskfallcrew](https://civitai.com/user/duskfallcrew/)
|Huggingface|[Earth & Dusk](https://huggingface.co/EarthnDusk)
|Ko-Fi| [Dusk's Kofi](https://ko-fi.com/duskfallcrew/)
