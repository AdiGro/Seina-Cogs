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

class SQLRole:
    allows_lambda: bool
    uses_inspection: bool

class UsesInspection:
    uses_inspection: bool

class AllowsLambdaRole:
    allows_lambda: bool

class HasCacheKeyRole(SQLRole): ...
class ExecutableOptionRole(SQLRole): ...
class LiteralValueRole(SQLRole): ...
class ColumnArgumentRole(SQLRole): ...
class ColumnArgumentOrKeyRole(ColumnArgumentRole): ...
class StrAsPlainColumnRole(ColumnArgumentRole): ...
class ColumnListRole(SQLRole): ...
class TruncatedLabelRole(SQLRole): ...
class ColumnsClauseRole(AllowsLambdaRole, UsesInspection, ColumnListRole): ...
class LimitOffsetRole(SQLRole): ...
class ByOfRole(ColumnListRole): ...
class GroupByRole(AllowsLambdaRole, UsesInspection, ByOfRole): ...
class OrderByRole(AllowsLambdaRole, ByOfRole): ...
class StructuralRole(SQLRole): ...
class StatementOptionRole(StructuralRole): ...
class OnClauseRole(AllowsLambdaRole, StructuralRole): ...
class WhereHavingRole(OnClauseRole): ...
class ExpressionElementRole(SQLRole): ...
class ConstExprRole(ExpressionElementRole): ...
class LabeledColumnExprRole(ExpressionElementRole): ...
class BinaryElementRole(ExpressionElementRole): ...
class InElementRole(SQLRole): ...
class JoinTargetRole(AllowsLambdaRole, UsesInspection, StructuralRole): ...
class FromClauseRole(ColumnsClauseRole, JoinTargetRole): ...

class StrictFromClauseRole(FromClauseRole):
    @property
    def description(self) -> None: ...

class AnonymizedFromClauseRole(StrictFromClauseRole): ...
class ReturnsRowsRole(SQLRole): ...
class StatementRole(SQLRole): ...

class SelectStatementRole(StatementRole, ReturnsRowsRole):
    def subquery(self) -> None: ...

class HasCTERole(ReturnsRowsRole): ...
class IsCTERole(SQLRole): ...
class CompoundElementRole(AllowsLambdaRole, SQLRole): ...
class DMLRole(StatementRole): ...
class DMLTableRole(FromClauseRole): ...
class DMLColumnRole(SQLRole): ...
class DMLSelectRole(SQLRole): ...
class DDLRole(StatementRole): ...
class DDLExpressionRole(StructuralRole): ...
class DDLConstraintColumnRole(SQLRole): ...
class DDLReferredColumnRole(DDLConstraintColumnRole): ...
