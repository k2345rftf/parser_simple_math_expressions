from unittest import TestCase
from Models.Expression.Context import Context
from Models.ExpParsers.StringExpParser import StringExpParser
import random, math


class TestStringParser(TestCase):

    def setUp(self) -> None:
        self.parser = StringExpParser()
        self.context = Context()

    def test_one_value(self):
        self.str_expr = f'{random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)
        # self.assertEqual(self.str_expr, expr.print())

    def test_one_var(self):
        self.str_expr = 'x'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(x, expr.eval())

    def test_all_operation_values(self):
        from math import sin, cos, tan, asin, acos, atan, sqrt, exp
        self.str_expr = f'{random.random()} + {random.random()} - {random.random()} * {random.random()} / {random.random()} + {random.random()}' \
                        f'+ sin({random.random()}) - cos({random.random()}) * asin({random.random()}) / acos({random.random()})' \
                        f'+ - exp({random.random()}) + tan({random.random()}) - atan({random.random()}) * sqrt({random.random()}) / ({random.random()})' \
                        f'+ - sin({random.random()})' \
                        f'+ - cos({random.random()})' \
                        f'+ - asin({random.random()})' \
                        f'+ - acos({random.random()})' \
                        f'+ - tan({random.random()})' \
                        f'+ - atan({random.random()})' \
                        f'+ - sqrt({random.random()})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_add_operations_values(self):
        self.str_expr = f'-{random.random()} + -{random.random()}'

        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_sub_operations_values(self):
        self.str_expr = f'-{random.random()} - -{random.random()}'
        # print(self.str_expr)
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_mul_operations_values(self):
        self.str_expr = f'-{random.random()} * -{random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_div_operations_values(self):
        self.str_expr = f'-{random.random()} / -{random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_pow_operations_values(self):
        x = -random.random()
        y = random.random()
        self.str_expr = f'{x}^{y}'
        expr = self.parser.parse_to_expression(self.str_expr)
        z1 = complex(pow(x, y))
        z2 = complex(expr.eval())
        self.assertLessEqual(z1.real - z2.real, 0.000000000001)
        self.assertLessEqual(z1.imag - z2.imag, 0.000000000001)


    def test_ln_values(self):
        import math
        x = random.random()+5
        self.str_expr = f'ln(x) + x'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.context.reg_var('x', x)
        expr.bind(self.context)
        self.assertEqual(math.log1p(x) + x, expr.eval())

    def test_e_values(self):
        import math
        self.str_expr = 'e + 1'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.e + 1, expr.eval())