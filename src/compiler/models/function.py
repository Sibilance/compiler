import typing

import attr

from . import statement


@attr.s(frozen=True, slots=True)
class Function:
    body: statement.Statement

    positional_arguments: typing.Sequence[str] = attr.ib(converter=tuple, default=())
    keyword_arguments: typing.Collection[str] = attr.ib(converter=frozenset, default=())
    extra_positional_arguments: typing.Optional[str] = attr.ib(default=None)
    extra_keyword_arguments: typing.Optional[str] = attr.ib(default=None)
