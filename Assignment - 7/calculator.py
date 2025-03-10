import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import os
from PyQt6 import uic
from model import CalculatorM

class CalculatorWin(QMainWindow):


    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), 'calc.ui')
        uic.loadUi(ui_path, self)

        self.calculator = CalculatorM()
        self.nullB.clicked.connect(lambda: self.on_click_digit('0'))
        self.oneB.clicked.connect(lambda:self.on_click_digit('1'))
        self.twoB.clicked.connect(lambda: self.on_click_digit('2'))
        self.threeB.clicked.connect(lambda: self.on_click_digit('3'))
        self.fourB.clicked.connect(lambda: self.on_click_digit('4'))
        self.fiveB.clicked.connect(lambda: self.on_click_digit('5'))
        self.sixB.clicked.connect(lambda: self.on_click_digit('6'))
        self.sevenB.clicked.connect(lambda: self.on_click_digit('7'))
        self.eightB.clicked.connect(lambda: self.on_click_digit('8'))
        self.nineB.clicked.connect(lambda: self.on_click_digit('9'))

        self.plusB.clicked.connect(lambda: self.on_click_operator('+'))
        self.minusB.clicked.connect(lambda: self.on_click_operator('-'))
        self.divideB.clicked.connect(lambda: self.on_click_operator('/'))
        self.multiplyB.clicked.connect(lambda: self.on_click_operator('*'))
        self.percentageB.clicked.connect(lambda: self.on_click_operator('%'))

        self.equalB.clicked.connect(lambda: self.on_click_equal())

        self.clearB.clicked.connect(lambda: self.on_click_clear)

        self.arrowB.clicked.connect(self.on_click_remove_last)

        self.negativeB.clicked.connect(self.on_click_toggle_negative)

        self.dotB.clicked.connect(self.on_click_dot)

    def on_click_digit(self, symbol):
        self.calculator.add_to_exp(symbol)
        self.input.setText(self.calculator.get_exp())

    def on_click_operator(self, op):
        self.calculator.add_to_exp(op)
        self.input.setText(self.calculator.get_exp())

    def on_click_equal(self):
        self.calculator.calculate()
        self.input.setText(self.calculator.get_exp())

    def on_click_clear(self):
        self.calculator.clear_exp()
        self.input.setText(self.calculator.get_exp())

    def on_click_remove_last(self):
        self.calculator.remove_last_char()  # Remove last char from expression
        self.input.setText(self.calculator.get_exp())  # Update display

    def on_click_toggle_negative(self):
        expression = self.calculator.get_exp()

        if expression:  # Ensure expression is not empty
            if expression.startswith('-'):
                self.calculator.expression = expression[1:]  # Remove '-'
            else:
                self.calculator.expression = '-' + expression  # Add '-'

        self.input.setText(self.calculator.get_exp())  # Update display

    def on_click_dot(self):
        if self.calculator.char != '.' and "." not in self.calculator.expression:  # Check only the last number
            self.calculator.add_to_exp('.')

        self.input.setText(self.calculator.get_exp())
        self.input.setText(self.calculator.get_exp())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = CalculatorWin()
    window.show()
    app.exec()

# pyqt6-tools designer