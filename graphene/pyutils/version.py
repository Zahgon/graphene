import datetime
import os
import subprocess


def get_version(version=None):
    "Returns a PEP 440-compliant version number from VERSION."
    version = get_complete_version(version)

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|rc}N - for alpha, beta, and rc releases

    main = get_main_version(version)

    sub = ""
    if version[3] == "alpha" and version[4] == 0:
        git_changeset = get_git_changeset()
        sub = ".dev%s" % git_changeset if git_changeset else ".dev"
    elif version[3] != "final":
        mapping = {"alpha": "a", "beta": "b", "rc": "rc"}
        sub = mapping[version[3]] + str(version[4])

    return str(main + sub)


def get_main_version(version=None):
    "Returns main version (X.Y[.Z]) from VERSION."
    pass


def get_complete_version(version=None):
    """Returns a tuple of the graphene version. If version argument is non-empty,
    then checks for correctness of the tuple provided.
    """
    pass


def get_docs_version(version=None):
    pass


def get_git_changeset():
    """Returns a numeric identifier of the latest git changeset.
    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    pass
