import graphene
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    # for registering the user.
    register = mutations.Register.Field()
    # for verifying a user account.
    verify_account = mutations.VerifyAccount.Field()
    # for logging in a user account.
    token_auth = mutations.ObtainJSONWebToken.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    pass
