import datetime

from dateutil.parser import isoparse

from graphql.error import GraphQLError
from graphql.language import StringValueNode, print_ast

from .scalars import Scalar


class Date(Scalar):
    """
    The `Date` scalar type represents a Date
    value as specified by
    [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
    """

    @staticmethod
    def serialize(date):
        pass

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pass

    @staticmethod
    def parse_value(value):
        pass


class DateTime(Scalar):
    """
    The `DateTime` scalar type represents a DateTime
    value as specified by
    [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
    """

    @staticmethod
    def serialize(dt):
        pass

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pass

    @staticmethod
    def parse_value(value):
        pass


class Time(Scalar):
    """
    The `Time` scalar type represents a Time value as
    specified by
    [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
    """

    @staticmethod
    def serialize(time):
        pass

    @classmethod
    def parse_literal(cls, node, _variables=None):
        pass

    @classmethod
    def parse_value(cls, value):
        pass
