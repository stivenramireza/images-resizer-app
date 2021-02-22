import os
import sys
import shutil
import asyncio
import aioboto3

from glob import glob
from PIL import Image
from fnmatch import fnmatch

from src.secrets import (
    SPACES_REGION,
    SPACES_BUCKET,
    SPACES_PREFIX,
    SPACES_ENDPOINT_URL,
    SPACES_ACCESS_KEY,
    SPACES_SECRET_KEY
)

from src.format import (
    get_filename,
    get_image_id
)

from src.logger import logger

LOCAL_IMAGES_PATH = sys.path[0]

async def download_file(key, bucket):
    if not key.endswith('/'):
        await bucket.download_file(key, key)
    elif not os.path.exists(key):
        os.makedirs(key)

async def download_files(bucket, prefix):
    async with aioboto3.resource('s3',
                                 region_name=SPACES_REGION,
                                 endpoint_url=SPACES_ENDPOINT_URL,
                                 aws_access_key_id=SPACES_ACCESS_KEY,
                                 aws_secret_access_key=SPACES_SECRET_KEY) as resource:
        bucket = await resource.Bucket(bucket)
        tasks = [asyncio.ensure_future(download_file(s3_obj.key, bucket)) async for s3_obj in
                 bucket.objects.filter(Prefix=prefix)]
        await asyncio.gather(*tasks)

async def download_images():
    try:
        await download_files(SPACES_BUCKET, SPACES_PREFIX)
        logger.info(f'Images from S3 have been downloaded successfully')
    except Exception as error:
        logger.error(f'Error to download images from S3: {error}')
        raise

async def upload_file(subdir, file, image, bucket):
    if fnmatch(file, f'{image.height}*.jpg'):
        full_path = os.path.join(subdir, file)
        with open(full_path, 'rb') as data:
            await bucket.put_object(ACL='public-read', Key=full_path[len(LOCAL_IMAGES_PATH) + 1:], Body=data,
                                    ContentType='image/jpg')

async def upload_files(bucket, prefix, image):
    tasks = []
    async with aioboto3.resource('s3',
                                 region_name=SPACES_REGION,
                                 endpoint_url=SPACES_ENDPOINT_URL,
                                 aws_access_key_id=SPACES_ACCESS_KEY,
                                 aws_secret_access_key=SPACES_SECRET_KEY) as resource:
        bucket = await resource.Bucket(bucket)
        for subdir, dirs, files in os.walk(LOCAL_IMAGES_PATH + f'/{prefix}'):
            for file in files:
                tasks.append(asyncio.ensure_future(upload_file(subdir, file, image, bucket)))
        await asyncio.gather(*tasks)

async def upload_images(image):
    try:
        await upload_files(SPACES_BUCKET, SPACES_PREFIX, image)
        logger.info('Images have been uploaded successfully into S3')
    except Exception as error:
        logger.error(f'Error to upload new images sizes to S3: {error}')
        raise

async def get_local_images():
    images = []
    for filename in glob(LOCAL_IMAGES_PATH + f'/{SPACES_PREFIX}/*/720*.jpg'):
        img = Image.open(filename)
        image = {
            "content": img,
            "image_id": get_image_id(filename),
            "filename": get_filename(filename)
        }
        images.append(image)
    return images

async def save_local_images(resized_images):
    try:
        for (i, new_image) in enumerate(resized_images):
            new_image['content'].save('{}/{}{}/{}{}'.format(LOCAL_IMAGES_PATH, SPACES_PREFIX, new_image['image_id'],
                                                            new_image['content'].height, new_image['filename']))
    except Exception as error:
        logger.error(f'Error to save images in local directories: {error}')
        raise

async def remove_local_images():
    path = os.path.join(LOCAL_IMAGES_PATH, 'test')
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        logger.info('Local images directory has been removed successfully')
    except shutil.Error as error:
        logger.error(f'Error to remove local images directory: {error}')
        raise