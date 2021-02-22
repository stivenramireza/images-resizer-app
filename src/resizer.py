from PIL import Image

async def resize_image(base_height, image):
    h_percent = (base_height / float(image['content'].size[1]))
    w_size = int((float(image['content'].size[0]) * float(h_percent)))
    image['content'] = image['content'].resize((w_size, base_height), Image.ANTIALIAS)
    return image

async def resize_images(base_height, images):
    resized_images = []
    for img in images:
        resized_img = await resize_image(base_height, img)
        resized_images.append(resized_img)
    return resized_images