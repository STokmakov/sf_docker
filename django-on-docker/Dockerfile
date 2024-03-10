FROM python:3.10
# Определяем переменные среды
# Чтобы python не создавал файлы .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Чтобы видеть выходные данные приложения в реальном времени
ENV PYTHONUNBUFFERED=1
# Создаем рабочую директорию
RUN mkdir -p /home/ubuntu/django/
# Устанавливаем рабочую директорию
WORKDIR /home/ubuntu/django/
# Копируем в рабочую директорию
COPY . .
# Обновляем pip, устанавливаем зависимости
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /home/ubuntu/django/requirements.txt
# copy entrypoint.sh
RUN sed -i 's/\r$//g' /home/ubuntu/django/entrypoint.sh
RUN chmod +x /home/ubuntu/django/entrypoint.sh
ENTRYPOINT ["/home/ubuntu/django/entrypoint.sh" ]
# Подключаем Volume
VOLUME /home/ubuntu/django/run/
# Указываем порт
EXPOSE 8000
# Запускаем gunicorn
RUN echo "$PWD"
RUN echo "$(ls -a)"
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "hello_django.wsgi:application" ]
