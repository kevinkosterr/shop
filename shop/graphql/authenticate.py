import json
import os

import requests
from rich import print as rprint


class GraphQLError(RuntimeError):
    pass


class GraphQLAuthenticationError(GraphQLError):
    pass


class GraphQLAuth:
    def __init__(self):
        self.uri = os.environ.get("GRAPHQL_URI")
        if not self.uri:
            raise GraphQLError(
                "No GRAPHQL_URI defined. Please define one in the environment variables."
            )

    def query(self, query, headers, variables=None):
        """Query the GraphQL backend.

        :param query: query to send to the GraphQL backend.
        :param headers: headers that get sent with the request.
        :param variables: variables for the query.
        :return: JSON response.
        """
        data = {"query": query, "variables": variables}
        h = {"Accept": "application/json", "Content-Type": "application/json"}
        # merge the two dictionaries
        headers = {**h, **headers}
        try:
            response = requests.post(
                self.uri,
                data=json.dumps(data),
                headers=headers,
                timeout=60,
            ).json()
        except requests.ReadTimeout as e:
            rprint(e)
            raise e

        if not response.get("data"):
            # If there are any errors, raise an Exception. This might be a little too much.
            raise GraphQLError(
                "Something went wrong while executing query. \n '{}' got no response.".format(
                    query
                )
            )

        return response

    def authenticate_user(self, token):
        """Authenticates the user through the GraphQL backend.

        :param token: token generated by request_token function, this is needed to authenticate the user.
        :return: Me (user) object.
        """
        query = """
            query Me{
                me{
                    id,
                    username,
                    email,
                }
            }
        """
        headers = {"Authorization": "JWT {}".format(token)}
        resp = self.query(query=query, headers=headers)
        if not resp["data"]["me"]:
            raise GraphQLAuthenticationError("No such user.")
        return resp["data"]["me"]

    def request_token(self, username, password):
        query = """
        mutation RequestAuthToken($username: String!, $password: String!){
            tokenAuth(username: $username, password: $password){
                success,
                errors,
                token,
                refreshToken,
            }
        }
        """
        vars = dict(username=username, password=password)
        resp = self.query(query=query, variables=vars, headers={})
        if resp["data"]["tokenAuth"]["errors"]:
            raise GraphQLAuthenticationError(
                "Something went wrong while trying to request a token for user.", resp
            )
        return resp["data"]["tokenAuth"]["token"]