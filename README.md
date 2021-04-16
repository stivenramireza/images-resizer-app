# Images Resizer App

FastAPI application to resize thousands of images asynchronously in few minutes from an S3 bucket.

<p align="center">
<img src="https://www.xnview.com/assets/img/app-resizeme-512.png">
</p>

## Run app in development mode

    $ pip install -r requirements.txt
    $ export PYTHON_ENV=development
    $ uvicorn src.main:app --reload

## Run app in production mode

    $ docker build -t images-resizer-app:latest .
	$ docker-compose up -d
