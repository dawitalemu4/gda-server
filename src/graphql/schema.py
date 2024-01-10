import graphene
from graphene_django import DjangoObjectType
from ..models.sale_clothes_model import sale_clothes_model
from ..models.sold_clothes_model import sold_clothes_model

class sale_clothes_type(DjangoObjectType):
    class Meta:
        model = sale_clothes_model
        fields = "__all__"

class sold_clothes_type(DjangoObjectType):
    class Meta:
        model = sold_clothes_model
        fields = "__all__"

class Query(graphene.ObjectType):
    saleClothes = graphene.List(sale_clothes_type)
    soldClothes = graphene.List(sold_clothes_type)

    def resolve_saleClothes(root, info):
        return sale_clothes_model.objects.all()
    
    def resolve_soldClothes(root, info):
        return sold_clothes_model.objects.all()

schema = graphene.Schema(query=Query)