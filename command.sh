# server
# Build docker image
docker build -t bibserver:latest -f Dockerfile-Server .

# start the container and listen on port 9999
docker run -it -p 8888:9999 -v "$pwd/save.json:/app/save.json" bibserver:latest


# client
# build image
docker build -t bibclient:latest -f Dockerfile-Client .

# run container
docker run -it bibclient:latest

# command to know the ip address of a docker container
docker inspect <container ID>