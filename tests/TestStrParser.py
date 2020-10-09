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

    def test_one_var(self):
        self.str_expr = 'x'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(x, expr.eval())

    def test_sin_var(self):
        self.str_expr = 'sin(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.sin(x), expr.eval())

    def test_cos_var(self):
        self.str_expr = 'cos(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.cos(x), expr.eval())

    def test_asin_var(self):
        self.str_expr = 'asin(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.asin(x), expr.eval())

    def test_acos_var(self):
        self.str_expr = 'acos(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.acos(x), expr.eval())

    def test_tan_var(self):
        self.str_expr = 'tan(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.tan(x), expr.eval())

    def test_atan_var(self):
        self.str_expr = 'atan(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.atan(x), expr.eval())

    def test_exp_var(self):
        self.str_expr = 'exp(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.exp(x), expr.eval())

    def test_sqrt_var(self):
        self.str_expr = 'sqrt(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.sqrt(x), expr.eval())

    def test_ln_var(self):
        self.str_expr = 'ln(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.log1p(x), expr.eval())

    def test_lg_var(self):
        self.str_expr = 'lg(x)'
        x = random.random()
        self.context.reg_var('x', x)
        expr = self.parser.parse_to_expression(self.str_expr)
        expr.bind(self.context)
        self.assertEqual(math.log10(x), expr.eval())

    def test_sin_value(self):
        x = random.random()
        self.str_expr = f'sin({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.sin(x), expr.eval())

    def test_cos_value(self):
        x = random.random()
        self.str_expr = f'cos({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.cos(x), expr.eval())

    def test_asin_value(self):
        x = random.random()
        self.str_expr = f'asin({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.asin(x), expr.eval())

    def test_acos_value(self):
        x = random.random()
        self.str_expr = f'acos({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.acos(x), expr.eval())

    def test_tan_value(self):
        x = random.random()
        self.str_expr = f'tan({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.tan(x), expr.eval())

    def test_atan_value(self):
        x = random.random()
        self.str_expr = f'atan({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.atan(x), expr.eval())

    def test_exp_value(self):
        x = random.random()
        self.str_expr = f'exp({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.exp(x), expr.eval())

    def test_sqrt_value(self):
        x = random.random()
        self.str_expr = f'sqrt({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.sqrt(x), expr.eval())

    def test_ln_value(self):
        x = random.random()
        self.str_expr = f'ln({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.log1p(x), expr.eval())

    def test_lg_value(self):
        x = random.random()
        self.str_expr = f'lg({x})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.log10(x), expr.eval())

    def test_all_operation_values(self):
        from math import sin, cos, tan, asin, acos, atan, sqrt, exp
        self.str_expr = f'{random.random()} + {random.random()} - {random.random()} * {random.random()} / {random.random()} + {random.random()}' \
                        f'+ sin({random.random()}) - cos({random.random()}) * asin({random.random()}) / acos({random.random()})' \
                        f'+ - exp({random.random()}) + tan({random.random()}) - atan({random.random()}) * sqrt({random.random()}) / ({random.random()})' \
                        f'+ + sin({random.random()})' \
                        f'+ - cos({random.random()})' \
                        f'+ + asin({random.random()})' \
                        f'+ - acos({random.random()})' \
                        f'+ + tan({random.random()})' \
                        f'+ - atan({random.random()})' \
                        f'+ + sqrt({random.random()})'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_add_operations_values(self):
        self.str_expr = f'-{random.random()} + -{random.random()}'

        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr)-expr.eval(), 0.000000000001)

    def test_uneg_sub_operations_values(self):
        self.str_expr = f'-{random.random()} - -{random.random()}'
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

    def test_e_const(self):
        import math
        self.str_expr = 'e'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.e, expr.eval())

    def test_pi_const(self):
        import math
        self.str_expr = 'pi'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertEqual(math.pi, expr.eval())

    def test_order_claculate_expr(self):
        self.str_expr = f'{random.random()} / {random.random()} + {random.random()} * {random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr) - expr.eval(), 0.000000000001)

    def test_order_pow_claculate_expr(self):
        self.str_expr = f'{random.random()} * {random.random()} ^ {random.random()} * {random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr.replace('^', '**')) - expr.eval(), 0.000000000001)

    def test_order_pow_claculate_expr_1(self):
        self.str_expr = f'{random.random()} + {random.random()} ^ {random.random()} * {random.random()}'
        expr = self.parser.parse_to_expression(self.str_expr)
        self.assertLessEqual(eval(self.str_expr.replace('^', '**')) - expr.eval(), 0.000000000001)
