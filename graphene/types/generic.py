from graphql.language.ast import (
    BooleanValueNode,
    FloatValueNode,
    IntValueNode,
    ListValueNode,
    ObjectValueNode,
    StringValueNode,
)

from graphene.types.scalars import MAX_INT, MIN_INT

from .scalars import Scalar


class GenericScalar(Scalar):
    """
    The `GenericScalar` scalar type represents a generic
    GraphQL scalar value that could be:
    String, Boolean, Int, Float, List or Object.
    """

    @staticmethod
    def identity(value):
        pass

    serialize = identity
    parse_value = identity

    @staticmethod
    def parse_literal(ast, _variables=None):
        pass
