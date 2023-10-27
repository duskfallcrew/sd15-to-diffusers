import argparse
import os
import torch
from diffusers import DiffusionPipeline
import kohya_ss.model_util as model_util

def convert_model(args):
    load_dtype = torch.float16 if args.fp16 else None
    save_dtype = get_save_dtype(args)

    is_load_checkpoint = determine_load_checkpoint(args.model_to_load)
    is_save_checkpoint = not is_load_checkpoint

    loaded_model_data = load_sd_model(args, is_load_checkpoint, load_dtype)
    convert_and_save_sd_model(args, is_save_checkpoint, loaded_model_data, save_dtype)

def get_save_dtype(args):
    if args.save_precision_as == "fp16":
        return torch.float16
    elif args.save_precision_as == "bf16":
        return torch.bfloat16
    elif args.save_precision_as == "float":
        return torch.float
    else:
        return None

def determine_load_checkpoint(model_to_load):
    if model_to_load.endswith('.ckpt') or model_to_load.endswith('.safetensors'):
        return True
    elif os.path.isdir(model_to_load):
        required_folders = {"unet", "text_encoder", "tokenizer", "scheduler", "vae"}
        if required_folders.issubset(set(os.listdir(model_to_load))) and os.path.isfile(os.path.join(model_to_load, "model_index.json")):
            return False
    return None

def load_sd_model(args, is_load_checkpoint, load_dtype):
    model_load_message = "checkpoint" if is_load_checkpoint else "Diffusion Model" + (" as fp16" if args.fp16 else "")
    print(f"Loading {model_load_message}: {args.model_to_load}")

    if is_load_checkpoint:
        loaded_model_data = load_from_sd_checkpoint(args)
    else:
        loaded_model_data = load_diffusion_model(args, load_dtype)

    return loaded_model_data

def load_from_sd_checkpoint(args):
    text_encoder1, vae, unet, _, _ = model_util.load_models_from_stable_diffusion_checkpoint(
        "stable-diffusion-v1-5", args.model_to_load, "cpu"
    )
    return text_encoder1, vae, unet

def load_diffusion_model(args, load_dtype):
    pipeline = DiffusionPipeline.from_pretrained(
        args.model_to_load, torch_dtype=load_dtype, tokenizer=None, scheduler=None
    )
    return pipeline.text_encoder, pipeline.vae, pipeline.unet

def convert_and_save_sd_model(args, is_save_checkpoint, loaded_model_data, save_dtype):
    text_encoder1, vae, unet = loaded_model_data
    model_save_message = "checkpoint" + ("" if save_dtype is None else f" in {save_dtype}") if is_save_checkpoint else "Diffusers"
    print(f"Converting and saving as {model_save_message}: {args.model_to_save}")

    if is_save_checkpoint:
        save_sd_as_checkpoint(args, text_encoder1, vae, unet, save_dtype)
    else:
        save_sd_as_diffusers(args, text_encoder1, vae, unet, save_dtype)

def save_sd_as_checkpoint(args, text_encoder1, vae, unet, save_dtype):
    logit_scale = None
    ckpt_info = None

    key_count = model_util.save_stable_diffusion_checkpoint(
        args.model_to_save, text_encoder1, unet, args.epoch, args.global_step, ckpt_info, vae, logit_scale, save_dtype
    )
    print(f"Model saved. Total converted state_dict keys: {key_count}")

def save_sd_as_diffusers(args, text_encoder1, vae, unet, save_dtype):
    reference_model_message = args.reference_model if args.reference_model is not None else 'default model'
    print(f"Copying scheduler/tokenizer config from: {reference_model_message}")
    sdxl_model_util.save_diffusers_checkpoint(
        args.model_to_save, text_encoder1, text_encoder2, unet, args.reference_model, vae, True, save_dtype
    )
    print(f"Model saved as {save_dtype}.")

def get_save_path(args, is_save_checkpoint):
    basename = os.path.splitext(args.model_to_load)[0]
    if is_save_checkpoint:
        return increment_filename(basename)
    else:
        return increment_filename(basename + ".safetensors")

def increment_filename(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base}({counter}){ext}"
        counter += 1
    return filename

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_to_load", type=str, required=True, help="model to load: checkpoint file or Diffusion model's directory")
    parser.add_argument("--fp16", action="store_true", help="load as fp16 (Diffusers only)")
    parser.add_argument("--save_precision_as", type=str, default="no", choices=["fp16", "bf16", "float"], help="save precision")
    parser.add_argument("--epoch", type=int, default=0, help="epoch to write to checkpoint")
    parser.add_argument("--global_step", type=int, default=0, help="global_step to write to checkpoint")
    parser.add_argument("--reference_model", type=str, default="runwayml/stable-diffusion-v1-5", help="reference Diffusers
