from Models.Interfaces import ParserInterface
from Models.Expression.Constants import *
from Models.Expression.Functions import *
from Models.Expression.SimpleOperations import *
from Models.ExpParsers.KindsOfToken import KindOfToken
from Models.ExpParsers.TokenParser import TokenParser


class StringExpParser(ParserInterface):

    def __init__(self):
        self.operations_in_base = {
            KindOfToken.NUMBER: self.__parse_value,
            KindOfToken.CHARS: self.__parse_chars,
            KindOfToken.ADD: self.__parse_sign_base,
            KindOfToken.SUB: self.__parse_sign_base,
            KindOfToken.LBRACE: self.__parse_expt_in_brace,
        }

        self.function = {
            KindOfToken.LN: LnExpr,
            KindOfToken.SIN: SinExpr,
            KindOfToken.COS: CosExpr,
            KindOfToken.TAN: TanExpr,
            KindOfToken.ATAN: ATanExpr,
            KindOfToken.ASIN: ASinExpr,
            KindOfToken.ACOS: ACosExpr,
            KindOfToken.SQRT: SqrtExpr,
            KindOfToken.EXP: ExpExpr,
            KindOfToken.LG: LgExpr,
        }

        self.constants = {
            'pi': PiConst,
            'e': EConst,
        }

        self.operations = {
            KindOfToken.ADD: AddExpr,
            KindOfToken.SUB: SubExpr,
            KindOfToken.MUL: MulExpr,
            KindOfToken.DIV: DivExpr,
            KindOfToken.POW: PowExpr,
        }

    def parse_to_expression(self, expression: str):
        self.__token_parser = TokenParser(expression)
        self.__next_token()
        expr = self.__parse_expression(self.__parse_expression)
        if self.token.kind_of_token != KindOfToken.EOL:
            raise ValueError('Extra characters after expression')
        return expr

    def parse_to_string(self, expression):
        return expression.print()

    def __parse_sign_base(self, token):
        self.__next_token()
        expr = self.__parse_base()
        return expr if token.kind_of_token == KindOfToken.ADD else UNegExpr(expr)

    def __parse_chars(self, token):
        self.__next_token()
        if token.string in self.constants:
            return self.constants[token.string]()
        return VarExpr(token.string)

    def __parse_func(self, token):
        self.__next_token()
        expr = self.function[token.kind_of_token](self.__parse_base())
        return expr

    def __parse_value(self, token) -> 'ExpressionInterface':
        self.__next_token()
        return ValueExpr(token.value)

    def __parse_expt_in_brace(self, token):
        self.__next_token()
        expression = self.__parse_expression(self.__parse_expression)
        if self.token.kind_of_token != KindOfToken.RBRACE:
            raise ValueError('expected )')
        self.__next_token()
        return expression

    def __parse_base(self) -> 'ExpressionInterface':
        if self.token.kind_of_token == KindOfToken.EOL:
            raise ValueError('Unexpected EOL')
        if self.token.kind_of_token in self.function:
            expression = self.__parse_func(self.token)
        elif self.token.kind_of_token in self.operations_in_base:
            expression = self.operations_in_base[self.token.kind_of_token](self.token)
        else:
            raise ValueError('Unexpected token')
        return expression

    def __next_token(self):
        self.token = self.__token_parser.get_next_token()

    def __parse_expression(self, operation=None) -> 'ExpressionInterface':
        if operation is None:
            operation = self.__parse_base
        arg = operation()
        while self.token.kind_of_token in self.operations:
            kind = self.token.kind_of_token
            self.__next_token()

            arg_1 = operation()
            arg = self.operations[kind](arg, arg_1)
        return arg
