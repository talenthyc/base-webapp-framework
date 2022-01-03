# Reference

- [Tutorial Flask](https://code.visualstudio.com/docs/python/tutorial-flask)

# How to run app locally

1. Run the command `cd src`, to change into the folder that contains the Flask app.
2. Run the command `set FLASK_APP=webapp` (Windows cmd) or `export set FLASK_APP=webapp` (macOS/Linux) to point to the app module.
3. Start the Flask server with `flask run`

# How to run app in docker

1. `docker build -t flask-webapp .`
2. `docker run -p 5000:5000 flask-webapp`
3. You can see the running webapp on `localhost:5000`

# How to enter docker container

- docker exec -it `docker ps | awk ' /flask-webapp/ { print $1 }'` bash

# Kill the docker container

- docker stop `docker ps | awk ' /flask-webapp/ { print $1 }'`


# How to deploy to Aliyun FC - [WIP]

- https://developer.aliyun.com/article/692174
