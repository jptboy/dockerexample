- [install docker ce](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)
- Do the above step with the "Install using the repository"
- [install docker compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)
- Just do step one of the guide above

- `sudo docker-compose build`
- `sudo docker-compose up`
- localhost:8080 is the url of the api
- type `localhost:8080/gettasks` in webbrowser to see tasks
- send `{"Name":"YOURTASK"}` as JSON through a post request to `localhost:8080/puttask` to add task
- send `{"Name":"YOURTASK"}` as JSON through a delete request to `localhost:8080/deltask` to delete task

- Use postman or insomnia `sudo snap install insomnia` for POST and DELETE request 

# FULLY WORKING REST-API WITH ITS OWN MONGODB INSTANCE BUILT!