

class RationalValueError(Exception):
    def __init__(self, operand1, operand2, message= "Неприпустимі аргументи!"):
        super().__init__()
        self.message = message
        self.operand1 = operand1
        self.operand2 = operand2

    def __str__(self):
        return f"{self.message}, {self.operand1= }, {self.operand2= }"