from Models.Interfaces import ExpressionInterface
from Models.Expression.Helper import add_bracets
import math

class ValueExpr(ExpressionInterface):
    _value: float

    def __init__(self, value: float):
        self._value = value

    def eval(self):
        return self._value

    def print(self, need_br=False):
        return str(self._value)

    def bind(self, context):
        pass


class VarExpr(ExpressionInterface):
    _name_var: str
    _value: float

    def __init__(self, name: str):
        self._name_var = name

    def bind(self, context):
        self._value = context.get_var(self._name_var)

    def eval(self):
        if self._value is None:
            raise ValueError(f'Unbound variable \"{self._name_var}\"')
        return self._value

    def print(self, need_br=False):
        return self._name_var


class UnaryExpr(ExpressionInterface):
    _arg: ExpressionInterface

    def __init__(self, arg: ExpressionInterface):
        self._arg = arg

    def bind(self, context):
        self._arg.bind(context)


class BinaryExpr(UnaryExpr):
    _arg_1: ExpressionInterface

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg)
        self._arg_1 = arg_1

    def _op_name(self) -> str:
        raise NotImplementedError

    def bind(self, context):
        self._arg_1.bind(context)
        self._arg.bind(context)

    def print(self, need_br=False):
        string = self._arg.print(True) + self._op_name() + self._arg_1.print(True)
        if need_br:
            string = add_bracets(string)
        return string


class UNegExpr(UnaryExpr):

    def __init__(self, arg: ExpressionInterface):
        super().__init__(arg)

    def eval(self):
        return -self._arg.eval()

    def print(self, need_br=False):
        string = '-' + self._arg.print()
        if need_br:
            string = add_bracets(string)
        return string


class AddExpr(BinaryExpr):

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg, arg_1)

    def _op_name(self):
        return '+'

    def eval(self):
        return self._arg.eval() + self._arg_1.eval()


class SubExpr(BinaryExpr):

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg, arg_1)

    def _op_name(self):
        return '-'

    def eval(self):
        return self._arg.eval() - self._arg_1.eval()


class MulExpr(BinaryExpr):

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg, arg_1)

    def _op_name(self):
        return '*'

    def eval(self):
        return self._arg.eval() * self._arg_1.eval()


class DivExpr(BinaryExpr):

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg, arg_1)

    def _op_name(self):
        return '/'

    def eval(self):
        try:
            return self._arg.eval() / self._arg_1.eval()
        except ZeroDivisionError:
            return math.inf if self._arg.eval() >= 0 else -math.inf


class PowExpr(BinaryExpr):

    def __init__(self, arg: ExpressionInterface, arg_1: ExpressionInterface):
        super().__init__(arg, arg_1)

    def _op_name(self):
        return '^'

    def eval(self):
        return pow(self._arg.eval(), self._arg_1.eval())