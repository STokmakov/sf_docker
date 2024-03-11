# Установка проекта с использованием чистого Docker (без использования docker-compos):

docker run --name sf_postgres -i -t -d sergeytokmakov/sf_postgres:latest

docker run --link sf_postgres:db --name sf_app -i -t -d sergeytokmakov/sf_app:latest

docker run --link sf_app:web -p 80:80 --name sf_nginx -i -t -d sergeytokmakov/sf_nginx:latest


# Запуск приложения http://127.0.0.1/admin

# user - admin

# password - admin
