from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    DJANGO_SUPERUSER_USERNAME='admin'
    DJANGO_SUPERUSER_EMAIL='admin@admin.com'
    DJANGO_SUPERUSER_PASSWORD='admin'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@admin.com'
        password = 'admin'

        if not User.objects.filter(username=username).exists():
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password)
        else:
            print('Admin account has already been initialized.')