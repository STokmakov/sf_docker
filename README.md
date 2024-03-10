sudo docker run --name sf_postgres -i -t -d sf_postgres:latest
sudo docker run --link sf_postgres:db --name sf_app -i -t -d sf_app:latest
sudo docker run --link sf_app:web -p 80:80 --name sf_nginx -i -t -d sf_nginx:latest
