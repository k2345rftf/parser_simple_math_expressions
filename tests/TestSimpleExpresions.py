from unittest import TestCase
from Models.Expression.Context import Context
from Models.Expression.Helper import add_bracets
from Models.Expression.SimpleOperations import *
import random

class TestValueExpressions(TestCase):

    def setUp(self) -> None:
        self.num = float(random.random())
        self.expr = ValueExpr(self.num)

    def test_value_expression(self):
        self.assertEqual(self.num, self.expr.eval(), 'Test 1')

    def test_string_expression(self):
        self.assertEqual(str(self.num), self.expr.print(), 'Test 2')

class TestVarExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.context = Context()
        self.context.reg_var('x', self.x)
        self.expr = VarExpr('x')
        self.expr.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(self.x, self.expr.eval(), 'Test 1')

    def test_string_expression(self):
        self.assertEqual('x', self.expr.print(), 'Test 2')


class TestUNegExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.context = Context()
        self.context.reg_var('x', self.x)
        var = VarExpr('x')
        self.expr = UNegExpr(var)
        self.expr.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(-self.x, self.expr.eval(), 'Test 1')

    def test_string_expression(self):
        self.assertEqual('-x', self.expr.print(False), 'Test 2')

class TestAddExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.y = float(random.random())

        value = ValueExpr(self.x)
        value_1 = ValueExpr(self.y)
        self.expr_with_values = AddExpr(value, value_1)

        self.context = Context()
        self.context.reg_var('x', self.x)
        self.context.reg_var('y', self.y)
        var = VarExpr('x')
        var_1 = VarExpr('y')
        self.expr_with_vars = AddExpr(var, var_1)
        self.expr_with_vars.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(self.x + self.y, self.expr_with_values.eval(), 'Test 1.1')
        self.assertEqual(self.x + self.y, self.expr_with_vars.eval(), 'Test 1.2')

    def test_string_expression(self):
        self.assertEqual(str(self.x)+'+'+str(self.y), self.expr_with_values.print(False), 'Test 2.1')
        self.assertEqual('x+y', self.expr_with_vars.print(False), 'Test 2.2')
        self.assertEqual('('+str(self.x)+'+'+str(self.y)+')', self.expr_with_values.print(True), 'Test 2.3')
        self.assertEqual('(x+y)', self.expr_with_vars.print(True), 'Test 2.4')


class TestSubExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.y = float(random.random())

        value = ValueExpr(self.x)
        value_1 = ValueExpr(self.y)
        self.expr_with_values = SubExpr(value, value_1)

        self.context = Context()
        self.context.reg_var('x', self.x)
        self.context.reg_var('y', self.y)
        var = VarExpr('x')
        var_1 = VarExpr('y')
        self.expr_with_vars = SubExpr(var, var_1)
        self.expr_with_vars.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(self.x - self.y, self.expr_with_values.eval(), 'Test 1.1')
        self.assertEqual(self.x - self.y, self.expr_with_vars.eval(), 'Test 1.2')

    def test_string_expression(self):
        self.assertEqual(str(self.x)+'-'+str(self.y), self.expr_with_values.print(False), 'Test 2.1')
        self.assertEqual('x-y', self.expr_with_vars.print(False), 'Test 2.2')
        self.assertEqual('('+str(self.x)+'-'+str(self.y)+')', self.expr_with_values.print(True), 'Test 2.3')
        self.assertEqual('(x-y)', self.expr_with_vars.print(True), 'Test 2.4')

class TestMulExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.y = float(random.random())

        value = ValueExpr(self.x)
        value_1 = ValueExpr(self.y)
        self.expr_with_values = MulExpr(value, value_1)

        self.context = Context()
        self.context.reg_var('x', self.x)
        self.context.reg_var('y', self.y)
        var = VarExpr('x')
        var_1 = VarExpr('y')
        self.expr_with_vars = MulExpr(var, var_1)
        self.expr_with_vars.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(self.x * self.y, self.expr_with_values.eval(), 'Test 1.1')
        self.assertEqual(self.x * self.y, self.expr_with_vars.eval(), 'Test 1.2')

    def test_string_expression(self):
        self.assertEqual(str(self.x)+'*'+str(self.y), self.expr_with_values.print(False), 'Test 2.1')
        self.assertEqual('x*y', self.expr_with_vars.print(False), 'Test 2.2')
        self.assertEqual('('+str(self.x)+'*'+str(self.y)+')', self.expr_with_values.print(True), 'Test 2.3')
        self.assertEqual('(x*y)', self.expr_with_vars.print(True), 'Test 2.4')

class TestDivExpressions(TestCase):

    def setUp(self) -> None:
        self.x = float(random.random())
        self.y = float(random.random())

        value = ValueExpr(self.x)
        value_1 = ValueExpr(self.y)
        self.expr_with_values = DivExpr(value, value_1)

        self.context = Context()
        self.context.reg_var('x', self.x)
        self.context.reg_var('y', self.y)
        var = VarExpr('x')
        var_1 = VarExpr('y')
        self.expr_with_vars = DivExpr(var, var_1)
        self.expr_with_vars.bind(self.context)

    def test_value_expression(self):
        self.assertEqual(self.x / self.y, self.expr_with_values.eval(), 'Test 1.1')
        self.assertEqual(self.x / self.y, self.expr_with_vars.eval(), 'Test 1.2')

    def test_string_expression(self):
        self.assertEqual(str(self.x)+'/'+str(self.y), self.expr_with_values.print(False), 'Test 2.1')
        self.assertEqual('x/y', self.expr_with_vars.print(False), 'Test 2.2')
        self.assertEqual('('+str(self.x)+'/'+str(self.y)+')', self.expr_with_values.print(True), 'Test 2.3')
        self.assertEqual('(x/y)', self.expr_with_vars.print(True), 'Test 2.4')

