import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from .mutations import Mutation

from shop.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        description = "A product"
        exclude = ["active"]


class Query(UserQuery, MeQuery, graphene.ObjectType):
    class Meta:
        description = (
            "Query object used to resolve queries with the GraphQL query language."
        )

    products = graphene.List(ProductType, description="Returns all active products.")
    product = graphene.Field(
        ProductType,
        uid=graphene.UUID(),
        description="Returns a product with the given UUID.",
    )

    def resolve_products(self, info, **kwargs):
        # TODO: should handle offset and limit.
        return Product.objects.all().filter(active=True)

    def resolve_product(self, uid):
        return Product.objects.get(uid=uid)


schema = graphene.Schema(query=Query, mutation=Mutation)
