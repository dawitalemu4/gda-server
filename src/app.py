from django.urls import path

from routes.sale_clothes_url import sale_clothes_urls
from routes.sold_clothes_url import sold_clothes_urls
from routes.admin_url import admin_urls

from controllers.sale_clothes_controller import sale_clothes_queries
from controllers.sold_clothes_controller import sold_clothes_queries
from controllers.admin_controller import admin_queries

urlpatterns = [
    
    path("", "Hello"),
    
    path(sale_clothes_urls["get_all_clothes"], sale_clothes_queries.get_all_clothes),
    path(sale_clothes_urls["get_clothing_by_id"], sale_clothes_queries.get_clothing_by_id),
    path(sale_clothes_urls["create_clothing"], sale_clothes_queries.create_clothing),
    path(sale_clothes_urls["update_clothing"], sale_clothes_queries.update_clothing),
    path(sale_clothes_urls["delete_clothing"], sale_clothes_queries.delete_clothing),
    
    path(sold_clothes_urls["get_all_clothes"], sold_clothes_queries.get_all_clothes),
    path(sold_clothes_urls["get_clothing_by_id"], sold_clothes_queries.get_clothing_by_id),
    path(sold_clothes_urls["create_clothing"], sold_clothes_queries.create_clothing),
    path(sold_clothes_urls["update_clothing"], sold_clothes_queries.update_clothing),
    path(sold_clothes_urls["delete_clothing"], sold_clothes_queries.delete_clothing),

    path(admin_urls["check_credentials"], admin_queries.check_credentials)

]

# add cors policy, and catch all to send 404 for undefined routes