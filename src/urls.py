from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .graphql.schema import schema

from .routes.sale_clothes_url import sale_clothes_urls
from .routes.sold_clothes_url import sold_clothes_urls
from .routes.admin_url import admin_urls

from .controllers.sale_clothes_controller import sale_clothes_queries
from .controllers.sold_clothes_controller import sold_clothes_queries
from .controllers.admin_controller import admin_queries

router = DefaultRouter()
router.register(r'auth', admin_queries, basename="auth")
router.register(r'sale_clothes', sale_clothes_queries, basename="sale_clothes")
router.register(r'sold_clothes', sold_clothes_queries, basename="sold_clothes")

urlpatterns = [

    path('', include(router.urls)),

    path('admin/', admin.site.urls),

    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
    path(sale_clothes_urls["get_all_clothes"], sale_clothes_queries.as_view({'get': 'get_all_clothes'})),
    path(sale_clothes_urls["get_clothing_by_id"], sale_clothes_queries.as_view({'get': 'get_clothing_by_id'})),
    path(sale_clothes_urls["create_clothing"], sale_clothes_queries.as_view({'post': 'create_clothing'})),
    path(sale_clothes_urls["update_clothing"], sale_clothes_queries.as_view({'put': 'update_clothing'})),
    path(sale_clothes_urls["delete_clothing"], sale_clothes_queries.as_view({'delete': 'delete_clothing'})),
    
    path(sold_clothes_urls["get_all_clothes"], sold_clothes_queries.as_view({'get': 'get_all_clothes'})),
    path(sold_clothes_urls["get_clothing_by_id"], sold_clothes_queries.as_view({'get': 'get_clothing_by_id'})),
    path(sold_clothes_urls["create_clothing"], sold_clothes_queries.as_view({'post': 'create_clothing'})),
    path(sold_clothes_urls["update_clothing"], sold_clothes_queries.as_view({'put': 'update_clothing'})),
    path(sold_clothes_urls["delete_clothing"], sold_clothes_queries.as_view({'delete': 'delete_clothing'})),
    
    path(admin_urls["check_credentials"], admin_queries.as_view({'get': 'check_credentials'}))
    
]

urlpatterns += router.urls