import sys
from PyQt6.QtWidgets import QApplication
#from mywindow import MyWindow




# mywindow.py
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit

class MyWindow(QMainWindow):
   def __init__(self):
       super().__init__()
       self.initUI()
       self.show()

   def initUI(self):
      self.setWindowTitle("My first GUI Application")
      self.setFixedSize(400, 300)

      self.label1 = QLabel("Hello World", self)
      self.label1.move(20, 20)

      self.input1 = QLineEdit(self)
      self.input1.move(20, 50)

      self.button1 = QtWidgets.QPushButton(self)
      self.button1.setText("Click Me")
      self.button1.move(20, 80)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyWindow()
   app.exec()