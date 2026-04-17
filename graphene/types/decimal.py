from decimal import Decimal as _Decimal

from graphql import Undefined
from graphql.language.ast import StringValueNode, IntValueNode

from .scalars import Scalar


class Decimal(Scalar):
    """
    The `Decimal` scalar type represents a python Decimal.
    """

    @staticmethod
    def serialize(dec):
        pass

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pass

    @staticmethod
    def parse_value(value):
        pass
