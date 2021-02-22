from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from src.model import Image
from src.logger import logger
from src.storage import download_images, get_local_images, save_local_images, upload_images, remove_local_images
from src.resizer import resize_images
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def generate(request: Request):
    return templates.TemplateResponse('image_resize.html', {"request": request})

@app.post("/generate")
async def generate_images(request: Request, image: Image = Depends(Image.as_form)):
    try:
        await download_images()
        resized_images = await resize_images(image.height, await get_local_images())
        print(resized_images)
        await save_local_images(resized_images)
        await upload_images(image)
        await remove_local_images()
        return templates.TemplateResponse('success_image_resize.html', {"request": request, "image": image})
    except Exception as error:
        logger.error(f'Error to generate images: {error}')
        return templates.TemplateResponse('error_image_resize.html', {"request": request})

def post_json(url, body):
    return requests.post(url, json=body)