# :whale: :potable_water: Docker / Flask boilerplate
### simple project template for easy prototyping


## Source the application
```bash

git clone https://github.com/minelminel/python-flask-docker-image.git

```

# Quick Setup (assuming you have Docker available locally)
```bash

bash deploy.sh

```


# Manual Setup

## Install Python modules

```python

   pip3 install -r requirements.txt

```


## Run the application using

```python

    python3 app.py

```


## Access site

```python

    http://localhost:5000

```

## Docker commands

```bash

        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath


        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>




```
