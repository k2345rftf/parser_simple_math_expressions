from Models.Expression.SimpleOperations import UnaryExpr, BinaryExpr
from Models.Expression.Helper import add_bracets
from Models.Interfaces import ExpressionInterface
import math


class UnaryFunc(UnaryExpr):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self) -> str:
        raise NotImplementedError

    def print(self, need_br=False):
        return self._func_name() + add_bracets(self._arg.print())


class LnExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'ln'

    def eval(self):
        return math.log1p(self._arg.eval())


class LgExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'lg'

    def eval(self):
        return math.log10(self._arg.eval())


class SinExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'sin'

    def eval(self):
        return math.sin(self._arg.eval())


class CosExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'cos'

    def eval(self):
        return math.cos(self._arg.eval())


class ASinExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'asin'

    def eval(self):
        return math.asin(self._arg.eval())


class ACosExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'acos'

    def eval(self):
        return math.acos(self._arg.eval())


class TanExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'tan'

    def eval(self):
        return math.tan(self._arg.eval())


class ATanExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'atan'

    def eval(self):
        return math.atan(self._arg.eval())


class SqrtExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'sqrt'

    def eval(self):
        return math.sqrt(self._arg.eval())


class ExpExpr(UnaryFunc):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def _func_name(self):
        return 'exp'

    def eval(self):
        return math.exp(self._arg.eval())
