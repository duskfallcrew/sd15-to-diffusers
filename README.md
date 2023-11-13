
# **SD 1.5 Model Converter**

<a target="_blank" href="https://colab.research.google.com/github/duskfallcrew/sd15-to-diffusers/blob/main/Converter_SD1_5_V2_FIXED.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


 **A Colab Notebook To Convert SD 1.5 Checkpoint to Diffusers format**

But a horribly duct taped edition. THIS IS IN ALPHA STAGES, WILL BE PATCHING THE CODE AS I GO ALONG.


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
