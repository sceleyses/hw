
class Rational:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, str):
            parts = numerator.split('/')
            if len(parts) != 2:
                raise ValueError("Неприпустимий формат рядка!")
            self.n = int(parts[0])
            self.d = int(parts[1])
            if denominator != 1:
                raise ValueError("Неприпустимі аргументи!")
        else:
            if not isinstance(numerator, int) or not isinstance(denominator, int):
                raise TypeError("Чисельник та знаменник повинні бути цілими числами!")
            self.n = numerator
            self.d = denominator

        if self.d == 0:
            raise ZeroDivisionError("На нуль ділити неможна!")

        self.reduce()

    @staticmethod
    def gcd(a, b):
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        common = self.gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Rational(other) - self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        if key == 'd':
            return self.d
        raise KeyError("Дозволені ключі: 'n' або 'd'")

    def __setitem__(self, key, value):
        if key not in ('n', 'd'):
            raise KeyError("Дозволені ключі: 'n' або 'd'")
        if not isinstance(value, int):
            raise TypeError("Значення має бути цілим числом")
        if key == 'd' and value == 0:
            raise ZeroDivisionError("Знаменник не може бути нулем")
        temp = Rational(self.n, self.d)
        if key == 'n':
            temp.n = value
        else:
            temp.d = value
        temp.reduce()
        self.n, self.d = temp.n, temp.d

    def __str__(self):
        return f"{self.n}/{self.d}"

if __name__ == "__main__":
    # r1 = Rational(5)
    # r2 = Rational(5, 6)
    # print(r1 + r2)
    #
    # r3 = Rational("5/3")
    # print(r3 + r3)
    #
    # r4 = Rational("10/2")
    # print(r4 * r1)
    #
    # # r5 = Rational(3, 0)
    # # print(r5)
    #
    # # r6 = Rational("4/2", 5)
    # # print(r6)
    #
    # r = Rational(2, 4)
    # print(r)
    # r['n'] = 7
    # print(r)
    # r['d'] = 4
    # print(r)

    def evaluate_expression(tokens):
        processed = []
        i = 0
        while i < len(tokens):
            current = tokens[i]
            if isinstance(current, str) and current == '*':
                left = processed.pop()
                i += 1
                right = tokens[i]
                processed.append(left * right)
            else:
                processed.append(current)
            i += 1

        result = processed[0]
        i = 1
        while i < len(processed):
            op = processed[i]
            right = processed[i + 1]
            if op == '+':
                result += right
            elif op == '-':
                result -= right
            i += 2
        return result


    try:
        with open("inputRational.txt") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                tokens = line.split()
                parsed = []
                for token in tokens:
                    if token in ('+', '-', '*'):
                        parsed.append(token)
                    else:
                        if '/' in token:
                            parsed.append(Rational(token))
                        else:
                            parsed.append(Rational(int(token)))
                try:
                    res = evaluate_expression(parsed)
                    print(res)
                except Exception as e:
                    print(f"Помилка у виразі '{line}': {e}")
    except FileNotFoundError:
        print("Файл inputRational.txt не знайдено.")