import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6 import uic

class Bmi(QMainWindow):
   def __init__(self):
       super().__init__()

       self.input1 = QLineEdit(self)
       self.input2 = QLineEdit(self)
       self.result = QLabel(self)
       self.button1 = QPushButton(self)

       ui_path = os.path.join(os.path.dirname(__file__), 'bmi.ui')
       uic.loadUi(ui_path, self)
       self.button1.clicked.connect(self.calculate)

   def calculate(self):
       try:
           weight = float(self.input1.text())
           height = float(self.input2.text()) / 100  # Convert cm to meters

           bmi = round(weight / (height ** 2), 2)

           return self.result.setText(str(bmi))

       except ValueError:
           self.result.setText("Invalid input!")

   def update(self):
       self.result.adjustSize()