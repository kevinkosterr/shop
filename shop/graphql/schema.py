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

    products = graphene.List(
        ProductType,
        offset=graphene.Int(),
        limit=graphene.Int(),
        description="Returns all active products.",
    )
    product = graphene.Field(
        ProductType,
        uid=graphene.UUID(),
        description="Returns a product with the given UUID.",
    )

    def resolve_products(self, info, offset=0, limit=9, **kwargs):
        """GraphQL for resolving the products query.

        :param info: filled by GraphQL.
        :param offset: offset for products query.
        :param limit: limit of products for the query.
        :param kwargs: other keyword arguments.
        :return: products from the database.
        """
        # we should only query active products, as the inactive ones aren't relevant to the user.
        _products = Product.objects.all().filter(active=True)

        if offset:
            # taking the offset into account.
            _products = _products[offset : offset + limit]

        # we're using slicing here, because Django's query sets are lazy.
        return _products[:limit]

    def resolve_product(self, uid):
        """GraphQL for resolving the product query.

        :param uid: uid of the product (UUID).
        :return: product from the database.
        """
        return Product.objects.get(uid=uid)


schema = graphene.Schema(query=Query, mutation=Mutation)
