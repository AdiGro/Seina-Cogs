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

from ..util import memoized_property
from . import elements

RESERVED_WORDS: Any
LEGAL_CHARACTERS: Any
LEGAL_CHARACTERS_PLUS_SPACE: Any
ILLEGAL_INITIAL_CHARACTERS: Any
FK_ON_DELETE: Any
FK_ON_UPDATE: Any
FK_INITIALLY: Any
BIND_PARAMS: Any
BIND_PARAMS_ESC: Any
BIND_TEMPLATES: Any
OPERATORS: Any
FUNCTIONS: Any
EXTRACT_MAP: Any
COMPOUND_KEYWORDS: Any
RM_RENDERED_NAME: int
RM_NAME: int
RM_OBJECTS: int
RM_TYPE: int

class ExpandedState(NamedTuple):
    statement: Any
    additional_parameters: Any
    processors: Any
    positiontup: Any
    parameter_expansion: Any

NO_LINTING: Any
COLLECT_CARTESIAN_PRODUCTS: Any
WARN_LINTING: Any
FROM_LINTING: Any

class FromLinter:
    def lint(self, start: Any | None = ...): ...
    def warn(self) -> None: ...

class Compiled:
    schema_translate_map: Any
    execution_options: Any
    compile_state: Any
    cache_key: Any
    dialect: Any
    preparer: Any
    statement: Any
    can_execute: Any
    string: Any
    def __init__(
        self, dialect, statement, schema_translate_map: Any | None = ..., render_schema_translate: bool = ..., compile_kwargs=...
    ) -> None: ...
    def visit_unsupported_compilation(self, element, err) -> None: ...
    @property
    def sql_compiler(self) -> None: ...
    def process(self, obj, **kwargs): ...
    def construct_params(self, params: Any | None = ..., extracted_parameters: Any | None = ...) -> None: ...
    @property
    def params(self): ...

class TypeCompiler:
    ensure_kwarg: str
    dialect: Any
    def __init__(self, dialect) -> None: ...
    def process(self, type_, **kw): ...
    def visit_unsupported_compilation(self, element, err, **kw) -> None: ...

class _CompileLabel(elements.ColumnElement[Any]):
    __visit_name__: str
    element: Any
    name: Any
    def __init__(self, col, name, alt_names=...) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw): ...

class SQLCompiler(Compiled):
    extract_map: Any
    compound_keywords: Any
    isdelete: bool
    isinsert: bool
    isupdate: bool
    isplaintext: bool
    returning: Any
    returning_precedes_values: bool
    render_table_with_column_in_update_from: bool
    ansi_bind_rules: bool
    insert_single_values_expr: Any
    literal_execute_params: Any
    post_compile_params: Any
    escaped_bind_names: Any
    has_out_parameters: bool
    insert_prefetch: Any
    update_prefetch: Any
    postfetch_lastrowid: bool
    positiontup: Any
    inline: bool
    column_keys: Any
    cache_key: Any
    for_executemany: Any
    linting: Any
    binds: Any
    bind_names: Any
    stack: Any
    positional: Any
    bindtemplate: Any
    ctes: Any
    label_length: Any
    anon_map: Any
    truncated_names: Any
    def __init__(
        self,
        dialect,
        statement,
        cache_key: Any | None = ...,
        column_keys: Any | None = ...,
        for_executemany: bool = ...,
        linting=...,
        **kwargs,
    ) -> None: ...
    @property
    def current_executable(self): ...
    @property
    def prefetch(self): ...
    def is_subquery(self): ...
    @property
    def sql_compiler(self): ...
    def construct_params(self, params: Any | None = ..., _group_number: Any | None = ..., _check: bool = ..., extracted_parameters: Any | None = ...): ...  # type: ignore[override]
    @property
    def params(self): ...
    def default_from(self): ...
    def visit_grouping(self, grouping, asfrom: bool = ..., **kwargs): ...
    def visit_select_statement_grouping(self, grouping, **kwargs): ...
    def visit_label_reference(self, element, within_columns_clause: bool = ..., **kwargs): ...
    def visit_textual_label_reference(self, element, within_columns_clause: bool = ..., **kwargs): ...
    def visit_label(
        self,
        label,
        add_to_result_map: Any | None = ...,
        within_label_clause: bool = ...,
        within_columns_clause: bool = ...,
        render_label_as_label: Any | None = ...,
        result_map_targets=...,
        **kw,
    ): ...
    def visit_lambda_element(self, element, **kw): ...
    def visit_column(
        self, column, add_to_result_map: Any | None = ..., include_table: bool = ..., result_map_targets=..., **kwargs
    ): ...
    def visit_collation(self, element, **kw): ...
    def visit_fromclause(self, fromclause, **kwargs): ...
    def visit_index(self, index, **kwargs): ...
    def visit_typeclause(self, typeclause, **kw): ...
    def post_process_text(self, text): ...
    def escape_literal_column(self, text): ...
    def visit_textclause(self, textclause, add_to_result_map: Any | None = ..., **kw): ...
    def visit_textual_select(self, taf, compound_index: Any | None = ..., asfrom: bool = ..., **kw): ...
    def visit_null(self, expr, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_tuple(self, clauselist, **kw): ...
    def visit_clauselist(self, clauselist, **kw): ...
    def visit_case(self, clause, **kwargs): ...
    def visit_type_coerce(self, type_coerce, **kw): ...
    def visit_cast(self, cast, **kwargs): ...
    def visit_over(self, over, **kwargs): ...
    def visit_withingroup(self, withingroup, **kwargs): ...
    def visit_funcfilter(self, funcfilter, **kwargs): ...
    def visit_extract(self, extract, **kwargs): ...
    def visit_scalar_function_column(self, element, **kw): ...
    def visit_function(self, func, add_to_result_map: Any | None = ..., **kwargs): ...
    def visit_next_value_func(self, next_value, **kw): ...
    def visit_sequence(self, sequence, **kw) -> None: ...
    def function_argspec(self, func, **kwargs): ...
    compile_state: Any
    def visit_compound_select(self, cs, asfrom: bool = ..., compound_index: Any | None = ..., **kwargs): ...
    def visit_unary(self, unary, add_to_result_map: Any | None = ..., result_map_targets=..., **kw): ...
    def visit_is_true_unary_operator(self, element, operator, **kw): ...
    def visit_is_false_unary_operator(self, element, operator, **kw): ...
    def visit_not_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_in_op_binary(self, binary, operator, **kw): ...
    def visit_empty_set_op_expr(self, type_, expand_op): ...
    def visit_empty_set_expr(self, element_types) -> None: ...
    def visit_binary(
        self,
        binary,
        override_operator: Any | None = ...,
        eager_grouping: bool = ...,
        from_linter: Any | None = ...,
        lateral_from_linter: Any | None = ...,
        **kw,
    ): ...
    def visit_function_as_comparison_op_binary(self, element, operator, **kw): ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_custom_op_binary(self, element, operator, **kw): ...
    def visit_custom_op_unary_operator(self, element, operator, **kw): ...
    def visit_custom_op_unary_modifier(self, element, operator, **kw): ...
    def visit_contains_op_binary(self, binary, operator, **kw): ...
    def visit_not_contains_op_binary(self, binary, operator, **kw): ...
    def visit_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw): ...
    def visit_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_not_endswith_op_binary(self, binary, operator, **kw): ...
    def visit_like_op_binary(self, binary, operator, **kw): ...
    def visit_not_like_op_binary(self, binary, operator, **kw): ...
    def visit_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_not_ilike_op_binary(self, binary, operator, **kw): ...
    def visit_between_op_binary(self, binary, operator, **kw): ...
    def visit_not_between_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw) -> None: ...
    def visit_bindparam(
        self,
        bindparam,
        within_columns_clause: bool = ...,
        literal_binds: bool = ...,
        skip_bind_expression: bool = ...,
        literal_execute: bool = ...,
        render_postcompile: bool = ...,
        **kwargs,
    ): ...
    def render_literal_bindparam(self, bindparam, render_literal_value=..., **kw): ...
    def render_literal_value(self, value, type_): ...
    def bindparam_string(
        self,
        name,
        positional_names: Any | None = ...,
        post_compile: bool = ...,
        expanding: bool = ...,
        escaped_from: Any | None = ...,
        **kw,
    ): ...
    execution_options: Any
    ctes_recursive: bool
    def visit_cte(
        self,
        cte,
        asfrom: bool = ...,
        ashint: bool = ...,
        fromhints: Any | None = ...,
        visiting_cte: Any | None = ...,
        from_linter: Any | None = ...,
        **kwargs,
    ): ...
    def visit_table_valued_alias(self, element, **kw): ...
    def visit_table_valued_column(self, element, **kw): ...
    def visit_alias(
        self,
        alias,
        asfrom: bool = ...,
        ashint: bool = ...,
        iscrud: bool = ...,
        fromhints: Any | None = ...,
        subquery: bool = ...,
        lateral: bool = ...,
        enclosing_alias: Any | None = ...,
        from_linter: Any | None = ...,
        **kwargs,
    ): ...
    def visit_subquery(self, subquery, **kw): ...
    def visit_lateral(self, lateral_, **kw): ...
    def visit_tablesample(self, tablesample, asfrom: bool = ..., **kw): ...
    def visit_values(self, element, asfrom: bool = ..., from_linter: Any | None = ..., **kw): ...
    def get_render_as_alias_suffix(self, alias_name_text): ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud): ...
    def get_select_hint_text(self, byfroms) -> None: ...
    def get_from_hint_text(self, table, text) -> None: ...
    def get_crud_hint_text(self, table, text) -> None: ...
    def get_statement_hint_text(self, hint_texts): ...
    translate_select_structure: Any
    def visit_select(
        self,
        select_stmt,
        asfrom: bool = ...,
        insert_into: bool = ...,
        fromhints: Any | None = ...,
        compound_index: Any | None = ...,
        select_wraps_for: Any | None = ...,
        lateral: bool = ...,
        from_linter: Any | None = ...,
        **kwargs,
    ): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_precolumns(self, select, **kw): ...
    def group_by_clause(self, select, **kw): ...
    def order_by_clause(self, select, **kw): ...
    def for_update_clause(self, select, **kw): ...
    def returning_clause(self, stmt, returning_cols) -> None: ...
    def limit_clause(self, select, **kw): ...
    def fetch_clause(self, select, **kw): ...
    def visit_table(
        self,
        table,
        asfrom: bool = ...,
        iscrud: bool = ...,
        ashint: bool = ...,
        fromhints: Any | None = ...,
        use_schema: bool = ...,
        from_linter: Any | None = ...,
        **kwargs,
    ): ...
    def visit_join(self, join, asfrom: bool = ..., from_linter: Any | None = ..., **kwargs): ...
    def visit_insert(self, insert_stmt, **kw): ...
    def update_limit_clause(self, update_stmt) -> None: ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None: ...
    def visit_update(self, update_stmt, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> None: ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms): ...
    def visit_delete(self, delete_stmt, **kw): ...
    def visit_savepoint(self, savepoint_stmt): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt): ...
    def visit_release_savepoint(self, savepoint_stmt): ...

class StrSQLCompiler(SQLCompiler):
    def visit_unsupported_compilation(self, element, err, **kw): ...
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_empty_set_expr(self, type_): ...
    def get_from_hint_text(self, table, text): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...

class DDLCompiler(Compiled):
    @memoized_property
    def sql_compiler(self): ...
    @memoized_property
    def type_compiler(self): ...
    def construct_params(self, params: Any | None = ..., extracted_parameters: Any | None = ...) -> None: ...
    def visit_ddl(self, ddl, **kwargs): ...
    def visit_create_schema(self, create, **kw): ...
    def visit_drop_schema(self, drop, **kw): ...
    def visit_create_table(self, create, **kw): ...
    def visit_create_column(self, create, first_pk: bool = ..., **kw): ...
    def create_table_constraints(self, table, _include_foreign_key_constraints: Any | None = ..., **kw): ...
    def visit_drop_table(self, drop, **kw): ...
    def visit_drop_view(self, drop, **kw): ...
    def visit_create_index(self, create, include_schema: bool = ..., include_table_schema: bool = ..., **kw): ...
    def visit_drop_index(self, drop, **kw): ...
    def visit_add_constraint(self, create, **kw): ...
    def visit_set_table_comment(self, create, **kw): ...
    def visit_drop_table_comment(self, drop, **kw): ...
    def visit_set_column_comment(self, create, **kw): ...
    def visit_drop_column_comment(self, drop, **kw): ...
    def get_identity_options(self, identity_options): ...
    def visit_create_sequence(self, create, prefix: Any | None = ..., **kw): ...
    def visit_drop_sequence(self, drop, **kw): ...
    def visit_drop_constraint(self, drop, **kw): ...
    def get_column_specification(self, column, **kwargs): ...
    def create_table_suffix(self, table): ...
    def post_create_table(self, table): ...
    def get_column_default_string(self, column): ...
    def visit_table_or_column_check_constraint(self, constraint, **kw): ...
    def visit_check_constraint(self, constraint, **kw): ...
    def visit_column_check_constraint(self, constraint, **kw): ...
    def visit_primary_key_constraint(self, constraint, **kw): ...
    def visit_foreign_key_constraint(self, constraint, **kw): ...
    def define_constraint_remote_table(self, constraint, table, preparer): ...
    def visit_unique_constraint(self, constraint, **kw): ...
    def define_constraint_cascades(self, constraint): ...
    def define_constraint_deferrability(self, constraint): ...
    def define_constraint_match(self, constraint): ...
    def visit_computed_column(self, generated, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw): ...
    def visit_REAL(self, type_, **kw): ...
    def visit_NUMERIC(self, type_, **kw): ...
    def visit_DECIMAL(self, type_, **kw): ...
    def visit_INTEGER(self, type_, **kw): ...
    def visit_SMALLINT(self, type_, **kw): ...
    def visit_BIGINT(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DATETIME(self, type_, **kw): ...
    def visit_DATE(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_CLOB(self, type_, **kw): ...
    def visit_NCLOB(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_BLOB(self, type_, **kw): ...
    def visit_BINARY(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_BOOLEAN(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_small_integer(self, type_, **kw): ...
    def visit_integer(self, type_, **kw): ...
    def visit_real(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_numeric(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_enum(self, type_, **kw): ...
    def visit_null(self, type_, **kw) -> None: ...
    def visit_type_decorator(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_, **kw): ...
    def __getattr__(self, key): ...
    def visit_null(self, type_, **kw): ...
    def visit_user_defined(self, type_, **kw): ...

class IdentifierPreparer:
    reserved_words: Any
    legal_characters: Any
    illegal_initial_characters: Any
    schema_for_object: Any
    dialect: Any
    initial_quote: Any
    final_quote: Any
    escape_quote: Any
    escape_to_quote: Any
    omit_schema: Any
    quote_case_sensitive_collations: Any
    def __init__(
        self,
        dialect,
        initial_quote: str = ...,
        final_quote: Any | None = ...,
        escape_quote: str = ...,
        quote_case_sensitive_collations: bool = ...,
        omit_schema: bool = ...,
    ) -> None: ...
    def validate_sql_phrase(self, element, reg): ...
    def quote_identifier(self, value): ...
    def quote_schema(self, schema, force: Any | None = ...): ...
    def quote(self, ident, force: Any | None = ...): ...
    def format_collation(self, collation_name): ...
    def format_sequence(self, sequence, use_schema: bool = ...): ...
    def format_label(self, label, name: Any | None = ...): ...
    def format_alias(self, alias, name: Any | None = ...): ...
    def format_savepoint(self, savepoint, name: Any | None = ...): ...
    def format_constraint(self, constraint, _alembic_quote: bool = ...): ...
    def truncate_and_render_index_name(self, name, _alembic_quote: bool = ...): ...
    def truncate_and_render_constraint_name(self, name, _alembic_quote: bool = ...): ...
    def format_index(self, index): ...
    def format_table(self, table, use_schema: bool = ..., name: Any | None = ...): ...
    def format_schema(self, name): ...
    def format_label_name(self, name, anon_map: Any | None = ...): ...
    def format_column(
        self,
        column,
        use_table: bool = ...,
        name: Any | None = ...,
        table_name: Any | None = ...,
        use_schema: bool = ...,
        anon_map: Any | None = ...,
    ): ...
    def format_table_seq(self, table, use_schema: bool = ...): ...
    def unformat_identifiers(self, identifiers): ...
