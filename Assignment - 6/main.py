import sys
from PyQt6.QtWidgets import QApplication
from bmi import Bmi

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Bmi()
   window.show()
   app.exec()


# pyqt6-tools designer