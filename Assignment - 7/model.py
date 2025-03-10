

class CalculatorM():
    def __init__(self):
        self.expression = ''
        self.char = ''

    def add_to_exp(self, char):
        self.expression = self.expression + char

    def remove_last_char(self):
        self.expression = self.expression[:-1]

    def clear_exp(self):
        self.expression = ''

    def calculate(self):
        if "%" in self.expression:
            parts = self.expression.split('%')
            if len(parts) == 2 and parts[0].strip().isdigit() and parts[1].strip().isdigit():
                base = float(parts[0])
                percent = float(parts[1])
                result = base * (percent / 100)
                self.expression = str(result)
                return result
        result = round(eval(self.expression), 3)
        self.expression = str(result)
        return result

    def get_exp(self):
        return self.expression

    def __str__(self):
        return self.expression

if __name__ == '__main__':

    calc = CalculatorM()
    calc.add_to_exp('100%20')
    calc.remove_last_char()
    print(calc.calculate())