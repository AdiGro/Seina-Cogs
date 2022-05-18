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

from typing import Any, NamedTuple

from .. import util
from .interfaces import LoaderStrategy

class UninstrumentedColumnLoader(LoaderStrategy):
    columns: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(
        self, compile_state, query_entity, path, loadopt, adapter, column_collection: Any | None = ..., **kwargs
    ) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class ColumnLoader(LoaderStrategy):
    logger: Any
    columns: Any
    is_composite: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, check_for_adapt: bool = ..., **kwargs) -> None: ...  # type: ignore[override]
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class ExpressionColumnLoader(ColumnLoader):
    logger: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, **kwargs) -> None: ...  # type: ignore[override]
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...

class DeferredColumnLoader(LoaderStrategy):
    logger: Any
    raiseload: Any
    columns: Any
    group: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def setup_query(self, compile_state, query_entity, path, loadopt, adapter, column_collection, memoized_populators, only_load_props: Any | None = ..., **kw) -> None: ...  # type: ignore[override]

class LoadDeferredColumns:
    key: Any
    raiseload: Any
    def __init__(self, key, raiseload: bool = ...) -> None: ...
    def __call__(self, state, passive=...): ...

class AbstractRelationshipLoader(LoaderStrategy):
    mapper: Any
    entity: Any
    target: Any
    uselist: Any
    def __init__(self, parent, strategy_key) -> None: ...

class DoNothingLoader(LoaderStrategy):
    logger: Any

class NoLoader(AbstractRelationshipLoader):
    logger: Any
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class LazyLoader(AbstractRelationshipLoader, util.MemoizedSlots):
    logger: Any
    is_aliased_class: Any
    use_get: Any
    def __init__(self, parent, strategy_key) -> None: ...
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class LoadLazyAttribute:
    key: Any
    strategy_key: Any
    loadopt: Any
    extra_criteria: Any
    def __init__(self, key, initiating_strategy, loadopt, extra_criteria) -> None: ...
    def __call__(self, state, passive=...): ...

class PostLoader(AbstractRelationshipLoader): ...

class ImmediateLoader(PostLoader):
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class SubqueryLoader(PostLoader):
    logger: Any
    join_depth: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...

    class _SubqCollections:
        session: Any
        execution_options: Any
        load_options: Any
        params: Any
        subq: Any
        def __init__(self, context, subq) -> None: ...
        def get(self, key, default): ...
        def loader(self, state, dict_, row) -> None: ...

    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators): ...

class JoinedLoader(AbstractRelationshipLoader):
    logger: Any
    join_depth: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def setup_query(
        self,
        compile_state,
        query_entity,
        path,
        loadopt,
        adapter,
        column_collection: Any | None = ...,
        parentmapper: Any | None = ...,
        chained_from_outerjoin: bool = ...,
        **kwargs,
    ) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators) -> None: ...

class SelectInLoader(PostLoader, util.MemoizedSlots):
    logger: Any

    class query_info(NamedTuple):
        load_only_child: Any
        load_with_join: Any
        in_expr: Any
        pk_cols: Any
        zero_idx: Any
        child_lookup_cols: Any
    join_depth: Any
    omit_join: Any
    def __init__(self, parent, strategy_key) -> None: ...
    def init_class_attribute(self, mapper) -> None: ...
    def create_row_processor(self, context, query_entity, path, loadopt, mapper, result, adapter, populators): ...

def single_parent_validator(desc, prop): ...
