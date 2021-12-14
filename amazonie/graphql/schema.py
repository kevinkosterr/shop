import graphene
from graphene_django import DjangoObjectType

from amazonie.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int())

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, id):
        return Product.objects.get(id=id)


schema = graphene.Schema(query=Query)
