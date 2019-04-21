# Installations
Try to use native linux and not a vm, it will be more speedy

- clone this repo and change your directory to be inside there
- `git clone https://github.com/jptboy/dockerexample.git`
- `cd dockerexample`
- [install docker ce](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)
    - `sudo apt-get update`
    - `sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo apt-key fingerprint 0EBFCD88`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
    - `sudo apt-get update`
    - `sudo apt-get install docker-ce docker-ce-cli containerd.io`
    - To test if it worked `sudo docker run hello-world`

- If your Ubuntu is not Ubuntu 16.xx the next step might not work, so lookup how to install docker compose for your version
- [install docker compose for ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)
    - ``sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose``
    - `sudo chmod +x /usr/local/bin/docker-compose`
    - To test if it worked `docker-compose --version`

# To run docker image

- Wait for these next two commands, they take a bit. Wait a couple minutes for the second one especially
    - Read the terminal output of docker-compose up to gauge when its done since the api wont work before the image is fully setup, and that might require some time
- `sudo docker-compose build`
- `sudo docker-compose up`
- `localhost:8080/gettasks` is the main url of the api
- type `localhost:8080/gettasks` in webbrowser to see tasks
- send `{"Name":"YOURTASK"}` as JSON through a POST request to `localhost:8080/puttask` to add task
    - refresh your browser, or go to `localhost:8080/gettasks` to check if the task got added
- send `{"Name":"YOURTASK"}` as JSON through a DELETE request to `localhost:8080/deltask` to delete task
    - refresh your browser, or go to `localhost:8080/gettasks` to check if the task got deleted

- Use postman or insomnia `sudo snap install insomnia` for POST and DELETE request 
    - to run insomnia type `insomnia` in terminal

# FULLY WORKING REST-API WITH ITS OWN MONGODB INSTANCE BUILT!
