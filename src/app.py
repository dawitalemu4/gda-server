from django.urls import path

from .routes.clothes_urls import clothes_urls

urlpatterns = [
    path("", "Hello"),
    path(clothes_urls.url.getAllCothes, controller),
]
