from binascii import Error as _Error
from base64 import b64decode, b64encode

from graphql.error import GraphQLError
from graphql.language import StringValueNode, print_ast

from .scalars import Scalar


class Base64(Scalar):
    """
    The `Base64` scalar type represents a base64-encoded String.
    """

    @staticmethod
    def serialize(value):
        pass

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pass

    @staticmethod
    def parse_value(value):
        pass
