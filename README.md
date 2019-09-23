# Object Tracking API


## Run application
### Run web application/service
    python manage.py runserver

### Run web application/service on port 80
    python manage.py runserver 0.0.0.0:8080

### Generate a requirements file
    pip freeze > requirements.txt

### Install required packages from requirements file
    pip install -r requirements.txt

### Migrate models to the database
    python manage.py makemigrations

### Sync the database to Create and make changes for tables
    python manage.py migrate

## REST API

### Get all the blocks
    /blocks/

### Get the latest blocks

    /blocks/latest/

### Get the block information given block id and signature/color

    /blocks/updated/?block_id=<block_id>&signature=<signature>