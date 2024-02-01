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


    saleClothes = graphene.List(sale_clothes_type, category=graphene.String(), size=graphene.String(), gender=graphene.String())

    def resolve_saleClothes(root, info, category=None, size=None, gender=None):

        if category and not size and not gender:
            return sale_clothes_model.objects.filter(category=category)
        if not category and size and not gender:
            return sale_clothes_model.objects.filter(size=size)
        if not category and not size and gender:
            return sale_clothes_model.objects.filter(gender=gender)
        if category and size and not gender:
            return sale_clothes_model.objects.filter(category=category, size=size)
        if category and not size and gender:
            return sale_clothes_model.objects.filter(category=category, gender=gender)
        if not category and size and gender:
            return sale_clothes_model.objects.filter(size=size, gender=gender)
        if category and size and gender:
            return sale_clothes_model.objects.filter(category=category, size=size, gender=gender)
        else:
            return sale_clothes_model.objects.all()


    soldClothes = graphene.List(sold_clothes_type, category=graphene.String(), size=graphene.String(), gender=graphene.String())

    def resolve_soldClothes(root, info, category=None, size=None, gender=None):

        if category and not size and not gender:
            return sold_clothes_model.objects.filter(category=category)
        if not category and size and not gender:
            return sold_clothes_model.objects.filter(size=size)
        if not category and not size and gender:
            return sold_clothes_model.objects.filter(gender=gender)
        if category and size and not gender:
            return sold_clothes_model.objects.filter(category=category, size=size)
        if category and not size and gender:
            return sold_clothes_model.objects.filter(category=category, gender=gender)
        if not category and size and gender:
            return sold_clothes_model.objects.filter(size=size, gender=gender)
        if category and size and gender:
            return sold_clothes_model.objects.filter(category=category, size=size, gender=gender)
        else:
            return sold_clothes_model.objects.all()
        

schema = graphene.Schema(query=Query)