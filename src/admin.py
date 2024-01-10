from django.contrib import admin
from .models.sale_clothes_model import sale_clothes_model
from .models.sold_clothes_model import sold_clothes_model

admin.site.register(sale_clothes_model)
admin.site.register(sold_clothes_model)