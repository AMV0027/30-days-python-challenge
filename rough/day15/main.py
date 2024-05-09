import torch
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

pipe.to("cuda")

prompt = "monkey eating a fried chicken in the moon0, realstic, 4k, octane render"

generator = torch.Generator("cuda").manual_seed(1024)
image = pipe(prompt, guidance_scale=7.5, num_inference_steps=20, generator=generator).images[0]

image.save(f"siva_prompt.png")