import pytest
from PIL import Image
from src.resizer import resize_image, resize_images

@pytest.fixture(scope='module')
def original_image():
    return {
        'content': Image.new('RGB', (960, 720)),
        'image_id': '10115',
        'filename': '327c079aae95344bbf0b02eb43a9afc9.jpg'
    }

@pytest.fixture(scope='module')
def resized_image_test():
    return {
        'content': Image.new('RGB', (146, 110)),
        'image_id': '10115',
        'filename': '327c079aae95344bbf0b02eb43a9afc9.jpg'
    }

@pytest.fixture(scope='module')
def original_images():
    return [
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10115',
            'filename': '327c079aae95344bbf0b02eb43a9afc9.jpg'
        },
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10115',
            'filename': '2813ac7ef4398c0c0b09f0e224e01db0.jpg'
        },
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10115',
            'filename': '104adefc5c747efcaa259e81796b0c0d.jpg'
        },
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10051', 'filename': '14e78983269a8bcd71682c3f3fd0c368.jpg'
        },
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10051',
            'filename': '12aa376a766c535b206276cc9fee3c8d.jpg'
        },
        {
            'content': Image.new('RGB', (960, 720)),
            'image_id': '10051',
            'filename': '1fae98d0002dc26b72a077e384b4717e.jpg'
        }
    ]

@pytest.fixture(scope='module')
def resized_images_test():
    return [
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10115',
            'filename': '327c079aae95344bbf0b02eb43a9afc9.jpg'
        },
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10115',
            'filename': '2813ac7ef4398c0c0b09f0e224e01db0.jpg'
        },
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10115',
            'filename': '104adefc5c747efcaa259e81796b0c0d.jpg'
        },
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10051',
            'filename': '14e78983269a8bcd71682c3f3fd0c368.jpg'
        },
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10051',
            'filename': '12aa376a766c535b206276cc9fee3c8d.jpg'
        },
        {
            'content': Image.new('RGB', (146, 110)),
            'image_id': '10051',
            'filename': '1fae98d0002dc26b72a077e384b4717e.jpg'
        }
    ]

async def test_resize_image(resized_image_test):
    resized_image = await resize_image(110, original_image)
    result = resized_image
    expected = resized_image_test
    assert result == expected

async def test_resize_images(original_images, resized_images_test):
    resized_images = await resize_images(110, original_images)
    result = resized_images
    expected = resized_images_test
    assert result == expected