

class RationalnError(ZeroDivisionError):
    def __init__(self, massege= "Знаменник не може бути 0, бо на 0 ділити не можна!"):
        self.massage = massege

    def __str__(self):
        return f"{self.massage}"

