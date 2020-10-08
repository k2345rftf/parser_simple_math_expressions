from PyQt5.QtWidgets import QMainWindow, QErrorMessage, QTableWidgetItem, QMessageBox

from Views.Ui_MainWidow import Ui_MainWindow

from Models.ExpParsers.StringExpParser import StringExpParser
from Models.Expression.Context import Context


class MainController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioButton.clicked.connect(self.change_x_mode)
        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.action.triggered.connect(self.help_user)
        self.parser = StringExpParser()

        self.context = Context()

    def help_user(self):
        msg = QMessageBox()
        msg.setText('В программе поддерживаются:\n'
                    'Числа в формате:\n'
                    '\t1e+1\n'
                    '\t10\n'
                    '\t10.0\n'
                    'Переменная со следующим именем:\n'
                    '\tx\n'
                    'Константы:\n'
                    '\te\n'
                    '\tpi\n'
                    'Функции:\n'
                    '\tln(x)\n'
                    '\tlg(x)\n'
                    '\texp(x)\n'
                    '\tsqrt(x)\n'
                    '\tsin(x)\n'
                    '\tcos(x)\n'
                    '\ttan(x)\n'
                    '\tasin(x)\n'
                    '\tacos(x)\n'
                    '\tatan(x)\n')
        msg.exec()

    def change_x_mode(self, event):
        if event:
            self.ui.verticalWidget.hide()
            self.ui.verticalWidget_2.show()
            self.ui.verticalWidget_3.show()
            self.ui.verticalWidget_4.show()
        else:
            self.ui.verticalWidget.show()
            self.ui.verticalWidget_2.hide()
            self.ui.verticalWidget_3.hide()
            self.ui.verticalWidget_4.hide()

    def calculate(self, event):
        string_expression = self.ui.textEdit.toPlainText().split('\n')
        try:
            if self.ui.radioButton.isChecked():
                x0 = self.ui.doubleSpinBox_2.value()
                x1 = self.ui.doubleSpinBox_3.value()
                if x0 <= x1:
                    error_msg = QErrorMessage(self)
                    error_msg.showMessage('Неправильный диапазон значений x0 должен быть меньше, чем x1')
                    return
                step = self.ui.doubleSpinBox_4.value()
                rez = []
                x = x0
                while x <= x1:
                    rez.append([x] + [self.__calc_expr(x, expr) for expr in string_expression])
                    x += step
                self.loadDataIntoTable(rez)

            else:
                x = self.ui.doubleSpinBox.value()
                rez = [[x] + [self.__calc_expr(x, expr) for expr in string_expression]]
                self.loadDataIntoTable(rez)
        except ValueError:
            error_msg = QErrorMessage(self)
            error_msg.showMessage('Данное выражение/переменная/функция/константа не поддерживаются в приложении или поле ввода пустое!!!')


    def __calc_expr(self, x, string_expression):
        expression = self.parser.parse_to_expression(string_expression)

        self.context.reg_var('x', x)
        expression.bind(self.context)
        return expression.eval()

    def loadDataIntoTable(self, data):
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setHorizontalHeaderLabels(['x', 'y'])
        [[self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j]))) for j in
          range(self.ui.tableWidget.columnCount())]for i in range(self.ui.tableWidget.rowCount())]


    def run(self):
        self.show()