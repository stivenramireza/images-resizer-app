import pytest
from src.format import get_image_id, get_filename

@pytest.fixture(scope='module')
def filename():
    return '/test/images/10115/720327c079aae95344bbf0b02eb43a9afc9.jpg'

@pytest.fixture(scope='module')
def get_image_id_test():
    return '10115'

@pytest.fixture(scope='module')
def get_filename_test():
    return '327c079aae95344bbf0b02eb43a9afc9.jpg'

def test_get_image_id(filename, get_image_id_test):
    result = get_image_id(filename)
    expected = get_image_id_test
    assert result == expected

def test_get_filename(filename, get_filename_test):
    result = get_filename(filename)
    expected = get_filename_test
    assert result == expected