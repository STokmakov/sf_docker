docker run --name sf_postgres -i -t -d sergeytokmakov/sf_postgres:latest

docker run --link sf_postgres:db --name sf_app -i -t -d sergeytokmakov/sf_app:latest

docker run --link sf_app:web -p 80:80 --name sf_nginx -i -t -d sergeytokmakov/sf_nginx:latest
