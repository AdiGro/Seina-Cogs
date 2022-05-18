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

from typing import Any

import sqlalchemy.types as sqltypes

from . import base as oracle
from .base import OracleCompiler, OracleDialect, OracleExecutionContext

class _OracleInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi): ...

class _OracleNumeric(sqltypes.Numeric):
    is_number: bool
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype) -> None: ...

class _OracleBinaryFloat(_OracleNumeric):
    def get_dbapi_type(self, dbapi): ...

class _OracleBINARY_FLOAT(_OracleBinaryFloat, oracle.BINARY_FLOAT): ...
class _OracleBINARY_DOUBLE(_OracleBinaryFloat, oracle.BINARY_DOUBLE): ...

class _OracleNUMBER(_OracleNumeric):
    is_number: bool

class _OracleDate(sqltypes.Date):
    def bind_processor(self, dialect) -> None: ...
    def result_processor(self, dialect, coltype): ...

class _OracleChar(sqltypes.CHAR):
    def get_dbapi_type(self, dbapi): ...

class _OracleNChar(sqltypes.NCHAR):
    def get_dbapi_type(self, dbapi): ...

class _OracleUnicodeStringNCHAR(oracle.NVARCHAR2):
    def get_dbapi_type(self, dbapi): ...

class _OracleUnicodeStringCHAR(sqltypes.Unicode):
    def get_dbapi_type(self, dbapi): ...

class _OracleUnicodeTextNCLOB(oracle.NCLOB):
    def get_dbapi_type(self, dbapi): ...

class _OracleUnicodeTextCLOB(sqltypes.UnicodeText):
    def get_dbapi_type(self, dbapi): ...

class _OracleText(sqltypes.Text):
    def get_dbapi_type(self, dbapi): ...

class _OracleLong(oracle.LONG):
    def get_dbapi_type(self, dbapi): ...

class _OracleString(sqltypes.String): ...

class _OracleEnum(sqltypes.Enum):
    def bind_processor(self, dialect): ...

class _OracleBinary(sqltypes.LargeBinary):
    def get_dbapi_type(self, dbapi): ...
    def bind_processor(self, dialect) -> None: ...
    def result_processor(self, dialect, coltype): ...

class _OracleInterval(oracle.INTERVAL):
    def get_dbapi_type(self, dbapi): ...

class _OracleRaw(oracle.RAW): ...

class _OracleRowid(oracle.ROWID):
    def get_dbapi_type(self, dbapi): ...

class OracleCompiler_cx_oracle(OracleCompiler):
    def bindparam_string(self, name, **kw): ...

class OracleExecutionContext_cx_oracle(OracleExecutionContext):
    out_parameters: Any
    include_set_input_sizes: Any
    def pre_exec(self) -> None: ...
    cursor_fetch_strategy: Any
    def post_exec(self) -> None: ...
    def create_cursor(self): ...
    def get_out_parameter_values(self, out_param_names): ...

class OracleDialect_cx_oracle(OracleDialect):
    supports_statement_cache: bool
    statement_compiler: Any
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_unicode_statements: bool
    supports_unicode_binds: bool
    use_setinputsizes: bool
    driver: str
    colspecs: Any
    execute_sequence_format: Any
    arraysize: Any
    encoding_errors: Any
    auto_convert_lobs: Any
    coerce_to_unicode: Any
    coerce_to_decimal: Any
    cx_oracle_ver: Any
    def __init__(
        self,
        auto_convert_lobs: bool = ...,
        coerce_to_unicode: bool = ...,
        coerce_to_decimal: bool = ...,
        arraysize: int = ...,
        encoding_errors: Any | None = ...,
        threaded: Any | None = ...,
        **kwargs,
    ): ...
    @classmethod
    def dbapi(cls): ...
    def initialize(self, connection) -> None: ...
    def get_isolation_level(self, connection): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def on_connect(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def create_xid(self): ...
    def do_executemany(self, cursor, statement, parameters, context: Any | None = ...) -> None: ...
    def do_begin_twophase(self, connection, xid) -> None: ...
    def do_prepare_twophase(self, connection, xid) -> None: ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_set_input_sizes(self, cursor, list_of_tuples, context) -> None: ...
    def do_recover_twophase(self, connection) -> None: ...

dialect = OracleDialect_cx_oracle
