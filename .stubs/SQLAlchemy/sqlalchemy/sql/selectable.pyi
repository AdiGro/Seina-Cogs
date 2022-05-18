"""
MIT License

Copyright (c) 2022-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from _typeshed import Self
from typing import Any

from .. import util
from ..util import HasMemoized, memoized_property
from . import roles, traversals, visitors
from .annotation import Annotated, SupportsCloneAnnotations
from .base import CacheableOptions, CompileState, Executable, Generative, HasCompileState, Immutable
from .elements import (
    BindParameter as BindParameter,
    BooleanClauseList as BooleanClauseList,
    ClauseElement as ClauseElement,
    ClauseList as ClauseList,
    ColumnClause as ColumnClause,
    GroupedElement as GroupedElement,
    Grouping as Grouping,
    TableValuedColumn as TableValuedColumn,
    UnaryExpression as UnaryExpression,
    literal_column as literal_column,
)

class _OffsetLimitParam(BindParameter[Any]):
    inherit_cache: bool

def subquery(alias, *args, **kwargs): ...

class ReturnsRows(roles.ReturnsRowsRole, ClauseElement):
    @property
    def selectable(self): ...
    @property
    def exported_columns(self) -> None: ...

class Selectable(ReturnsRows):
    __visit_name__: str
    is_selectable: bool
    def lateral(self, name: Any | None = ...): ...
    def replace_selectable(self, old, alias): ...
    def corresponding_column(self, column, require_embedded: bool = ...): ...

class HasPrefixes:
    def prefix_with(self: Self, *expr, **kw) -> Self: ...

class HasSuffixes:
    def suffix_with(self: Self, *expr, **kw) -> Self: ...

class HasHints:
    def with_statement_hint(self, text, dialect_name: str = ...): ...
    def with_hint(self: Self, selectable, text: str, dialect_name: str = ...) -> Self: ...

class FromClause(roles.AnonymizedFromClauseRole, Selectable):
    __visit_name__: str
    named_with_column: bool
    schema: Any
    is_selectable: bool
    def select(self, whereclause: Any | None = ..., **kwargs): ...
    def join(self, right, onclause: Any | None = ..., isouter: bool = ..., full: bool = ...): ...
    def outerjoin(self, right, onclause: Any | None = ..., full: bool = ...): ...
    def alias(self, name: Any | None = ..., flat: bool = ...): ...
    def table_valued(self): ...
    def tablesample(self, sampling, name: Any | None = ..., seed: Any | None = ...): ...
    def is_derived_from(self, fromclause): ...
    @property
    def description(self): ...
    @property
    def exported_columns(self): ...
    @memoized_property
    def columns(self): ...
    @property
    def entity_namespace(self): ...
    @memoized_property
    def primary_key(self): ...
    @memoized_property
    def foreign_keys(self): ...
    @property
    def c(self): ...

LABEL_STYLE_NONE: Any
LABEL_STYLE_TABLENAME_PLUS_COL: Any
LABEL_STYLE_DISAMBIGUATE_ONLY: Any
LABEL_STYLE_DEFAULT: Any

class Join(roles.DMLTableRole, FromClause):
    __visit_name__: str
    left: Any
    right: Any
    onclause: Any
    isouter: Any
    full: Any
    def __init__(self, left, right, onclause: Any | None = ..., isouter: bool = ..., full: bool = ...) -> None: ...
    @property
    def description(self): ...
    def is_derived_from(self, fromclause): ...
    def self_group(self, against: Any | None = ...): ...
    def select(self, whereclause: Any | None = ..., **kwargs): ...
    @property
    def bind(self): ...
    def alias(self, name: Any | None = ..., flat: bool = ...): ...

class NoInit:
    def __init__(self, *arg, **kw) -> None: ...

class AliasedReturnsRows(NoInit, FromClause):
    named_with_column: bool
    @property
    def description(self): ...
    @property
    def original(self): ...
    def is_derived_from(self, fromclause): ...
    @property
    def bind(self): ...

class Alias(roles.DMLTableRole, AliasedReturnsRows):
    __visit_name__: str
    inherit_cache: bool

class TableValuedAlias(Alias):
    __visit_name__: str
    @HasMemoized.memoized_attribute
    def column(self): ...
    def alias(self, name: Any | None = ...): ...  # type: ignore[override]
    def lateral(self, name: Any | None = ...): ...
    def render_derived(self, name: Any | None = ..., with_types: bool = ...): ...

class Lateral(AliasedReturnsRows):
    __visit_name__: str
    inherit_cache: bool

class TableSample(AliasedReturnsRows):
    __visit_name__: str

class CTE(roles.DMLTableRole, roles.IsCTERole, Generative, HasPrefixes, HasSuffixes, AliasedReturnsRows):
    __visit_name__: str
    def alias(self, name: Any | None = ..., flat: bool = ...): ...
    def union(self, *other): ...
    def union_all(self, *other): ...

class HasCTE(roles.HasCTERole):
    def add_cte(self, cte) -> None: ...
    def cte(self, name: Any | None = ..., recursive: bool = ..., nesting: bool = ...): ...

class Subquery(AliasedReturnsRows):
    __visit_name__: str
    inherit_cache: bool
    def as_scalar(self): ...

class FromGrouping(GroupedElement, FromClause):
    element: Any
    def __init__(self, element) -> None: ...
    @property
    def columns(self): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...
    def is_derived_from(self, element): ...
    def alias(self, **kw): ...

class TableClause(roles.DMLTableRole, Immutable, FromClause):
    __visit_name__: str
    named_with_column: bool
    implicit_returning: bool
    name: Any
    primary_key: Any
    foreign_keys: Any
    schema: Any
    fullname: Any
    def __init__(self, name, *columns, **kw) -> None: ...
    @memoized_property
    def description(self): ...
    def append_column(self, c, **kw) -> None: ...
    def insert(self, values: Any | None = ..., inline: bool = ..., **kwargs): ...
    def update(self, whereclause: Any | None = ..., values: Any | None = ..., inline: bool = ..., **kwargs): ...
    def delete(self, whereclause: Any | None = ..., **kwargs): ...

class ForUpdateArg(ClauseElement):
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    nowait: Any
    read: Any
    skip_locked: Any
    key_share: Any
    of: Any
    def __init__(
        self, nowait: bool = ..., read: bool = ..., of: Any | None = ..., skip_locked: bool = ..., key_share: bool = ...
    ) -> None: ...

class Values(Generative, FromClause):
    named_with_column: bool
    __visit_name__: str
    name: Any
    literal_binds: Any
    def __init__(self, *columns, **kw) -> None: ...
    def alias(self: Self, name: Any | None, **kw) -> Self: ...  # type: ignore[override]
    def lateral(self: Self, name: Any | None = ...) -> Self: ...
    def data(self: Self, values) -> Self: ...

class SelectBase(
    roles.SelectStatementRole,
    roles.DMLSelectRole,
    roles.CompoundElementRole,
    roles.InElementRole,
    HasCTE,
    Executable,
    SupportsCloneAnnotations,
    Selectable,
):
    is_select: bool
    @property
    def selected_columns(self) -> None: ...
    @property
    def exported_columns(self): ...
    @property
    def c(self): ...
    @property
    def columns(self): ...
    def select(self, *arg, **kw): ...
    def as_scalar(self): ...
    def exists(self): ...
    def scalar_subquery(self): ...
    def label(self, name): ...
    def lateral(self, name: Any | None = ...): ...
    def subquery(self, name: Any | None = ...): ...
    def alias(self, name: Any | None = ..., flat: bool = ...): ...

class SelectStatementGrouping(GroupedElement, SelectBase):
    __visit_name__: str
    element: Any
    def __init__(self, element) -> None: ...
    def get_label_style(self): ...
    def set_label_style(self, label_style): ...
    @property
    def select_statement(self): ...
    def self_group(self, against: Any | None = ...): ...
    @property
    def selected_columns(self): ...

class DeprecatedSelectBaseGenerations:
    def append_order_by(self, *clauses) -> None: ...
    def append_group_by(self, *clauses) -> None: ...

class GenerativeSelect(DeprecatedSelectBaseGenerations, SelectBase):
    def __init__(
        self,
        _label_style=...,
        use_labels: bool = ...,
        limit: Any | None = ...,
        offset: Any | None = ...,
        order_by: Any | None = ...,
        group_by: Any | None = ...,
        bind: Any | None = ...,
    ) -> None: ...
    def with_for_update(
        self: Self, nowait: bool = ..., read: bool = ..., of: Any | None = ..., skip_locked: bool = ..., key_share: bool = ...
    ) -> Self: ...
    def get_label_style(self): ...
    def set_label_style(self, style): ...
    def apply_labels(self): ...
    def limit(self: Self, limit: Any | None) -> Self: ...
    def fetch(self: Self, count: Any | None, with_ties: bool = ..., percent: bool = ...) -> Self: ...
    def offset(self: Self, offset: Any | None) -> Self: ...
    def slice(self: Self, start: Any | None, stop: Any | None) -> Self: ...
    def order_by(self: Self, *clauses) -> Self: ...
    def group_by(self: Self, *clauses) -> Self: ...

class CompoundSelectState(CompileState): ...

class CompoundSelect(HasCompileState, GenerativeSelect):
    __visit_name__: str
    UNION: Any
    UNION_ALL: Any
    EXCEPT: Any
    EXCEPT_ALL: Any
    INTERSECT: Any
    INTERSECT_ALL: Any
    keyword: Any
    selects: Any
    def __init__(self, keyword, *selects, **kwargs) -> None: ...
    def self_group(self, against: Any | None = ...): ...
    def is_derived_from(self, fromclause): ...
    @property
    def selected_columns(self): ...
    @property
    def bind(self): ...
    @bind.setter
    def bind(self, bind) -> None: ...

class DeprecatedSelectGenerations:
    def append_correlation(self, fromclause) -> None: ...
    def append_column(self, column) -> None: ...
    def append_prefix(self, clause) -> None: ...
    def append_whereclause(self, whereclause) -> None: ...
    def append_having(self, having) -> None: ...
    def append_from(self, fromclause) -> None: ...

class SelectState(util.MemoizedSlots, CompileState):
    class default_select_compile_options(CacheableOptions): ...
    statement: Any
    from_clauses: Any
    froms: Any
    columns_plus_names: Any
    def __init__(self, statement, compiler, **kw) -> None: ...
    @classmethod
    def get_column_descriptions(cls, statement) -> None: ...
    @classmethod
    def from_statement(cls, statement, from_statement) -> None: ...
    @classmethod
    def get_columns_clause_froms(cls, statement): ...
    @classmethod
    def determine_last_joined_entity(cls, stmt): ...
    @classmethod
    def all_selected_columns(cls, statement): ...

class _SelectFromElements: ...

class _MemoizedSelectEntities(traversals.HasCacheKey, traversals.HasCopyInternals, visitors.Traversible):
    __visit_name__: str

class Select(
    HasPrefixes, HasSuffixes, HasHints, HasCompileState, DeprecatedSelectGenerations, _SelectFromElements, GenerativeSelect
):
    __visit_name__: str
    @classmethod
    def create_legacy_select(
        cls,
        columns: Any | None = ...,
        whereclause: Any | None = ...,
        from_obj: Any | None = ...,
        distinct: bool = ...,
        having: Any | None = ...,
        correlate: bool = ...,
        prefixes: Any | None = ...,
        suffixes: Any | None = ...,
        **kwargs,
    ): ...
    def __init__(self) -> None: ...
    def filter(self, *criteria): ...
    def filter_by(self, **kwargs): ...
    @property
    def column_descriptions(self): ...
    def from_statement(self, statement): ...
    def join(self: Self, target, onclause: Any | None = ..., isouter: bool = ..., full: bool = ...) -> Self: ...
    def outerjoin_from(self, from_, target, onclause: Any | None = ..., full: bool = ...): ...
    def join_from(self: Self, from_, target, onclause: Any | None = ..., isouter: bool = ..., full: bool = ...) -> Self: ...
    def outerjoin(self, target, onclause: Any | None = ..., full: bool = ...): ...
    def get_final_froms(self): ...
    @property
    def froms(self): ...
    @property
    def columns_clause_froms(self): ...
    @property
    def inner_columns(self): ...
    def is_derived_from(self, fromclause): ...
    def get_children(self, **kwargs): ...
    def add_columns(self: Self, *columns) -> Self: ...
    def column(self, column): ...
    def reduce_columns(self, only_synonyms: bool = ...): ...
    def with_only_columns(self: Self, *columns, **kw) -> Self: ...
    @property
    def whereclause(self): ...
    def where(self: Self, *whereclause) -> Self: ...
    def having(self: Self, having) -> Self: ...
    def distinct(self: Self, *expr) -> Self: ...
    def select_from(self: Self, *froms) -> Self: ...
    def correlate(self: Self, *fromclauses) -> Self: ...
    def correlate_except(self: Self, *fromclauses) -> Self: ...
    @HasMemoized.memoized_attribute
    def selected_columns(self): ...
    def self_group(self, against: Any | None = ...): ...
    def union(self, *other, **kwargs): ...
    def union_all(self, *other, **kwargs): ...
    def except_(self, *other, **kwargs): ...
    def except_all(self, *other, **kwargs): ...
    def intersect(self, *other, **kwargs): ...
    def intersect_all(self, *other, **kwargs): ...
    @property
    def bind(self): ...
    @bind.setter
    def bind(self, bind) -> None: ...

class ScalarSelect(roles.InElementRole, Generative, Grouping):
    inherit_cache: bool
    element: Any
    type: Any
    def __init__(self, element) -> None: ...
    @property
    def columns(self) -> None: ...
    @property
    def c(self): ...
    def where(self: Self, crit) -> Self: ...
    def self_group(self, **kwargs): ...
    def correlate(self: Self, *fromclauses) -> Self: ...
    def correlate_except(self: Self, *fromclauses) -> Self: ...

class Exists(UnaryExpression):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def select(self, whereclause: Any | None = ..., **kwargs): ...
    def correlate(self, *fromclause): ...
    def correlate_except(self, *fromclause): ...
    def select_from(self, *froms): ...
    def where(self, *clause): ...

class TextualSelect(SelectBase):
    __visit_name__: str
    is_text: bool
    is_select: bool
    element: Any
    column_args: Any
    positional: Any
    def __init__(self, text, columns, positional: bool = ...) -> None: ...
    @HasMemoized.memoized_attribute
    def selected_columns(self): ...
    def bindparams(self: Self, *binds, **bind_as_values) -> Self: ...

TextAsFrom = TextualSelect

class AnnotatedFromClause(Annotated):
    def __init__(self, element, values) -> None: ...
