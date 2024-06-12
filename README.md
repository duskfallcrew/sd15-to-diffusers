
# **SD 1.5 Model Converter**


> # **SD 1.5 Model Converter**
> **A Colab Notebook To Convert SD 1.5 Checkpoint to Diffusers format**
> This was patched heavily and recoded from the SDXL branch of Linaqruf's now archived colab. We're porting our patches to our github with gracious credit to the original coders.



> ## **Instructions**


Before diving in, ensure you create a Hugging Face token with write permissions. Follow this link for instructions on token creation.

You need to create a huggingface token, go to [this link](https://huggingface.co/settings/tokens), then `create new token` or copy available token with the `Write` role.

>

| Step | Instructions | 
| --- | --- | 
|♻ - |Install/Clone etc
|♻ -|Download model 
|♻ -| Put your model details in.
|♻ -|DUMP PATH = folder name
|♻ -| If your downloaded model is safetensors please tick the box.
|♻ - |Check file browser, if the model/yourmodelhere looks like a diffusers format you're good to go!
|♻ -| Write Token + Set up your Repo!
|♻ - |Upload Diffusers!

>

| Link Name| Description | Link |
| --- | --- | --- |
| [Huggingface Backup](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb) | backup checkpoints! | [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/kieranxsomer/HuggingFace_Backup/blob/main/HuggingFace_Backup.ipynb)
| [SD 1.5 Conversion to Diffusers](https://colab.research.google.com/drive/1zAzdsaa2KQcF6W0V4eCLZ6eUO8hsDJTo?usp=drive_link)| Convert SD 1.5 to Diffusers| [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/drive/1zAzdsaa2KQcF6W0V4eCLZ6eUO8hsDJTo?usp=drive_link)
| [SDXL Conversion to Diffusers](https://colab.research.google.com/drive/1CcSCmUB_UkT-8TlUkwDDKnHB4T7nti01?usp=drive_link)| Convert SDXL to Diffusers| [![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/drive/1CcSCmUB_UkT-8TlUkwDDKnHB4T7nti01?usp=drive_link)
|Discord| E&D Discord |[Invite](https://discord.gg/5t2kYxt7An)
|CivitAi| Duskfallcrew @ Civitai |[Duskfallcrew](https://civitai.com/user/duskfallcrew/)
|Huggingface| E&D Huggingface |[Earth & Dusk](https://huggingface.co/EarthnDusk)
|Ko-Fi| Kofi Support |[![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/Z8Z8L4EO)
|Github| Duskfallcrew Github |[Duskfallcrew](https://github.com/duskfallcrew)
| Youtube: | Duskfall Music|[Duskfall Music & More](https://www.youtube.com/channel/UCk7MGP7nrJz5awBSP75xmVw)
| Spotify: | E&D Royalty Free| [PLAYLIST](https://open.spotify.com/playlist/00R8x00YktB4u541imdSSf?si=57a8f0f0fe87434e)
|DA Group | AI Group| [DeviantArt Group](https://www.deviantart.com/diffusionai)
| Reddit | Earth & Dusk| [Subreddit](https://www.reddit.com/r/earthndusk/)



> ## Collaboration


I am NOT A programmer by nature, I patch with what little knowledge I have. I Failed programming several times over the years, so if something needs cleaning up and you want to patch it - pull request it!


>## About 


We are a system of over 300 alters, proudly navigating life with Dissociative Identity Disorder, ADHD, Autism, and CPTSD. We believe in the potential of AI to break down barriers and enhance aspects of mental health, even as it presents challenges. Our creative journey is an ongoing exploration of identity and expression, and we invite you to join us in this adventure.



>Future ideas:

- Looking to port PT to safetensors into the same notebook.

- Looking to figure out how to manage to get the conversions to roll on google drive for more space options.
- Porting it to VastAi/Runpod

Cancelled Ideas that don't make sense for this product
- Looking to port inference for testing into the same notebook. - Not sure why you'd need this unless you're training, I think this was in the SDXL one from Linaqruf, but this isn't required on this one.
- Looking to figure out how to convert a different vae. - I could NOT get this to work no matter what I did. I have some THEORIES, but i'm not a programmer.




>## Credits:


| Patched Origin | Description | Link |
| --- | --- | --- |
|Patched from| ARCHIVED |[SDXL - Linaqruf](https://colab.research.google.com/github/Linaqruf/sdxl-model-converter/blob/main/sdxl_model_converter.ipynb)
|***Linaqruf @ Github***: |https://github.com/Linaqruf
|Linaqruf Ko-Fi | [![](https://dcbadge.vercel.app/api/shield/850007095775723532?style=flat)](https://lookup.guru/850007095775723532) [![ko-fi](https://img.shields.io/badge/Support%20me%20on%20Ko--fi-F16061?logo=ko-fi&logoColor=white&style=flat)](https://ko-fi.com/linaqruf) 
| Linaqruf Saweria |<a href="https://saweria.co/linaqruf"><img alt="Saweria" src="https://img.shields.io/badge/Saweria-7B3F00?style=flat&logo=ko-fi&logoColor=white"/></a>
