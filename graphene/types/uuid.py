from uuid import UUID as _UUID

from graphql.error import GraphQLError
from graphql.language.ast import StringValueNode
from graphql import Undefined

from .scalars import Scalar


class UUID(Scalar):
    """
    Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects
    in fields, resolvers and input.
    """

    @staticmethod
    def serialize(uuid):
        pass

    @staticmethod
    def parse_literal(node, _variables=None):
        pass

    @staticmethod
    def parse_value(value):
        pass
