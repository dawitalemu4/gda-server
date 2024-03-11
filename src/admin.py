from django.contrib import admin
from django.contrib.auth.models import User
from .models.sale_clothes_model import sale_clothes_model
from .models.sold_clothes_model import sold_clothes_model
from dotenv import dotenv_values
env = dotenv_values(".env")

if not User.objects.filter(username=env['DJANGO_USER']).exists():
    user = User.objects.create_user(env['DJANGO_USER'], email=env['DJANGO_EMAIL'], password=env['DJANGO_PASSWORD'])
    user.is_superuser = True
    user.is_staff = True
    user.save()

admin.site.register(sale_clothes_model)
admin.site.register(sold_clothes_model)