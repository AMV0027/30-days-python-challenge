from diffusers import DiffusionPipeline
import torch

#https://huggingface.co/docs/diffusers/stable_diffusion


model_id = "ogkalu/Comic-Diffusion"
pipeline = DiffusionPipeline.from_pretrained(model_id, use_safetensors=True)

prompt = input("enter yout prompt : ")

pipeline = pipeline.to("cuda")
generator = torch.Generator("cuda").manual_seed(0)
image = pipeline(prompt, generator=generator, num_inference_steps=10).images[0]

image.save(f"image_gen.png")

