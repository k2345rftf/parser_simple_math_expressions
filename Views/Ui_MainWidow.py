# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 370)
        MainWindow.setMinimumSize(QtCore.QSize(680, 370))
        MainWindow.setMaximumSize(QtCore.QSize(680, 370))
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(8, 8, 647, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalWidget = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        self.verticalWidget.setMinimumSize(QtCore.QSize(87, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalWidget)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMinimum(-99999999.999)
        self.doubleSpinBox.setMaximum(99999999.999)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.verticalWidget_2 = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(87, 0))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(-99999999.999)
        self.doubleSpinBox_2.setMaximum(99999999.999)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalWidget_3 = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        self.verticalWidget_3.setMinimumSize(QtCore.QSize(87, 0))
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalWidget_3)
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMinimum(-99999999.999)
        self.doubleSpinBox_3.setMaximum(99999999.999)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout.addWidget(self.verticalWidget_3)
        self.verticalWidget_4 = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(87, 0))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.verticalWidget_4)
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMinimum(0.001)
        self.doubleSpinBox_4.setMaximum(99999999.999)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout_4.addWidget(self.doubleSpinBox_4)
        self.horizontalLayout.addWidget(self.verticalWidget_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.verticalLayoutWidget_5)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер выражений"))
        self.label.setText(_translate("MainWindow", "Введите значение x:"))
        self.label_2.setText(_translate("MainWindow", "Значение"))
        self.label_3.setText(_translate("MainWindow", "От"))
        self.label_4.setText(_translate("MainWindow", "До"))
        self.label_5.setText(_translate("MainWindow", "Шаг"))
        self.radioButton.setText(_translate("MainWindow", "Интервал"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Справка"))
        self.verticalWidget_2.hide()
        self.verticalWidget_3.hide()
        self.verticalWidget_4.hide()
