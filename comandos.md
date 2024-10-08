docker build -t app-react .
docker run it app-react sh
docker container prune
docker image prune
docker images
docker image rm app-react:1
docker image tag app-react:latest app-react:1