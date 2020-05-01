# Docker commands

### Listing 

    $ docker ps  // Running containers

    $ docker images // Images

    $ docker container ls // Existing containers

### Deleting

    $ docker kill $(docker ps -q) // Running containers

    $ docker rm $(docker ps -a -q) // Delete all stopped containers
    
    $ docker rmi $(docker images -q) // Delete all images

### Get into container

    $ docker exec -i -t <container-name-or-id> bash
