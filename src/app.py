from django.urls import path

from .routes.sale_clothes_url import sale_clothes_url
from .controllers.sale_clothes_controller import sold_clothes_queries

urlpatterns = [
    path(" ", "Hello"),
    path(sale_clothes_url.get_all_clothes, sold_clothes_queries.get_all_sale_clothes),
]