from PyQt5.QtWidgets import QApplication
import sys

from Controller.MainController import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainController()
    window.run()
    sys.exit(app.exec_())
