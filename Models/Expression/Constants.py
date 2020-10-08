from Models.Interfaces import ExpressionInterface
import math


class ConstExpr(ExpressionInterface):
    def __init__(self, name: str, value: float):
        self.__name = name
        self.__value = value



    def eval(self):
        return self.__value

    def print(self, need_br):
        return self.__name

    def bind(self, context):
        pass

class PiConst(ConstExpr):

    def __init__(self):
        super().__init__('pi', math.pi)

class EConst(ConstExpr):

    def __init__(self):
        super().__init__('e', math.e)

