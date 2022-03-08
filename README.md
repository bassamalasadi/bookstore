# BookStore

-------------------------------------------------------
## Docker


> ### Note
> I assume  that you already installed `docker` and `docker-compose`
> Install `docker` : https://docs.docker.com/get-docker/
> Install `docker compose` : https://docs.docker.com/compose/install/


Clone the project to your local environment

```
git clone https://github.com/bassamalasadi/bookstore.git
```
Navigate to the repo
```sh
cd bookstore
```

### Build the project
```sh
docker-compose build
```
### Run the project
```sh
docker-compose up
```
It will run on : `127.0.0.1:8000` or `0.0.0.0:8000`
### Test the project
```sh
docker-compose run bookstore python manage.py test
```

## License

MIT
