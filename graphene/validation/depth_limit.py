# This is a Python port of https://github.com/stems/graphql-depth-limit
# which is licensed under the terms of the MIT license, reproduced below.
#
# -----------
#
# MIT License
#
# Copyright (c) 2017 Stem
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

try:
    from re import Pattern
except ImportError:
    # backwards compatibility for v3.6
    from typing import Pattern
from typing import Callable, Dict, List, Optional, Union, Tuple

from graphql import GraphQLError
from graphql.validation import ValidationContext, ValidationRule
from graphql.language import (
    DefinitionNode,
    FieldNode,
    FragmentDefinitionNode,
    FragmentSpreadNode,
    InlineFragmentNode,
    Node,
    OperationDefinitionNode,
)

from ..utils.is_introspection_key import is_introspection_key


IgnoreType = Union[Callable[[str], bool], Pattern, str]


def depth_limit_validator(
    max_depth: int,
    ignore: Optional[List[IgnoreType]] = None,
    callback: Optional[Callable[[Dict[str, int]], None]] = None,
):
    pass


def get_fragments(
    definitions: Tuple[DefinitionNode, ...],
) -> Dict[str, FragmentDefinitionNode]:
    pass


# This will actually get both queries and mutations.
# We can basically treat those the same
def get_queries_and_mutations(
    definitions: Tuple[DefinitionNode, ...],
) -> Dict[str, OperationDefinitionNode]:
    pass


def determine_depth(
    node: Node,
    fragments: Dict[str, FragmentDefinitionNode],
    depth_so_far: int,
    max_depth: int,
    context: ValidationContext,
    operation_name: str,
    ignore: Optional[List[IgnoreType]] = None,
) -> int:
    pass


def is_ignored(node: FieldNode, ignore: Optional[List[IgnoreType]] = None) -> bool:
    pass
