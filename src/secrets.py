import os
from dotenv import load_dotenv

from src.logger import logger

PYTHON_ENV = os.environ.get('PYTHON_ENV')
if PYTHON_ENV == 'production':
    dotenv_path = '.env'
    logger.info('Using production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Using development environment variables')

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

PORT = os.environ.get('PORT')
PYTHON_ENV = os.environ.get('PYTHON_ENV')

SPACES_REGION = os.environ.get('SPACES_REGION')
SPACES_BUCKET = os.environ.get('SPACES_BUCKET')
SPACES_PREFIX = os.environ.get('SPACES_PREFIX')
SPACES_ENDPOINT_URL = os.environ.get('SPACES_ENDPOINT_URL')
SPACES_ACCESS_KEY = os.environ.get('SPACES_ACCESS_KEY')
SPACES_SECRET_KEY = os.environ.get('SPACES_SECRET_KEY')