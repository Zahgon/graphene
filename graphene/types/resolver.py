def attr_resolver(attname, default_value, root, info, **args):
    pass


def dict_resolver(attname, default_value, root, info, **args):
    pass


def dict_or_attr_resolver(attname, default_value, root, info, **args):
    pass


default_resolver = dict_or_attr_resolver


def set_default_resolver(resolver):
    pass


def get_default_resolver():
    pass
