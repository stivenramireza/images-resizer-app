# Images Resizer App

FastAPI application to resize thousands of images asynchronously in few minutes from an S3 bucket.

<p align="center">
<img src="https://lh3.googleusercontent.com/proxy/Xd08GiQXvzojzjIXWCSGq9zIt5d2rH4eQ6DYHK1SSribvmuxxYkD_sF8X8asIuT9ftm61fYXO3cCIvCf5tgMBTGdkRjbPzdB83WZ11bIgHkg96PHrgf8VF10d8AZGyMM9s9_4c01">
</p>

## Run app in development mode

    $ pip install -r requirements.txt
    $ export PYTHON_ENV=development
    $ uvicorn src.main:app --reload

## Run app in production mode

    $ docker build -t images-resizer-app:latest .
	$ docker-compose up -d