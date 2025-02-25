'''import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit

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

#from mywindow import MyWindow
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyWindow()
   app.exec()
'''


import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6 import uic

class MyWindow(QMainWindow):
   def __init__(self):
       super().__init__()
       self.label1 : QLabel
       self.input1 : QLineEdit
       self.button1 : QPushButton
       ui_path = os.path.join(os.path.dirname(__file__), "resources/l_16.ui")
       uic.loadUi(ui_path, self)
       self.button1.clicked.connect(self.on_button1_click)

   def on_button1_click(self):
       txt = self.input1.text()
       self.label1.setText(txt)

import sys
from PyQt6.QtWidgets import QApplication

#from mywindow import MyWindow


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyWindow()
   window.show()
   app.exec()
