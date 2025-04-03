class Rational:
    def __init__(self,numerator, denominator=1 ):
        if isinstance(numerator, str):
            parts = numerator.split('/')
            if len(parts) == 2:
                self.n = int(parts[0])
                self.d = int(parts[1])
            else:
                raise ValueError("Неприпустимий формат!")

            if denominator != 1:
                raise ValueError("Неприпустиме значення!")
        else:
            if not isinstance(numerator, int) or not isinstance(denominator, int):
                raise TypeError("Чисельник та знаменник повинні бути цілими числами!")
            self.n = numerator
            self.d = denominator

        if self.d == 0:
            raise ValueError("На нуль ділити неможна!")

    def __add__(self, other):
        new_n = self.n * other.d + other.n * self.d
        if self.d != other.d:
            new_d = self.d * other.d
        else:
            new_d = self.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        new_n = self.n * other.d - other.n * self.d
        if self.d != other.d:
            new_d = self.d * other.d
        else:
            new_d = self.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)


    def __str__(self):
            return f"{self.n}/{self.d}"

if __name__ == "__main__":
    r1 = Rational(5)
    r2 = Rational(5, 6)
    print(r1 + r2)

    r3 = Rational("5/3")
    print(r3 + r3)

    r4 = Rational("10/2")
    print(r4 * r1)

    # r5 = Rational(3, 0)
    # print(r5)

    # r6 = Rational("4/2", 5)
    # print(r6)
