from Rational import Rational
class RationalList(list):
    def __init__(self, iterable):
        for item in iterable:
            self.validate(item)
        super().__init__(iterable)

    def validate(self, item):
        if not isinstance(item, (Rational, int)):
            raise TypeError("Елементи повинні бути типу Rational або int")
        if isinstance(item, int):
            return Rational(item)
        return item

    def __setitem__(self, key, value):
        value = self.validate(value)
        super().__setitem__(key, value)

    def append(self, item):
        item = self.validate(item)
        super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            for item in other:
                self.append(item)

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(super().__add__(other))
        other = self.validate(other)
        return type(self)(super().__add__([other]))

    def __iadd__(self, other):
        if isinstance(other, (type(self), list)):
            self.extend(other)
        else:
            self.append(other)
        return self

    def sum(self):
        total = Rational(0)
        for num in self:
            if isinstance(num, int):
                num = Rational(num)
            total += num
        return total


def evaluate_expression(tokens):
    processed = []
    i = 0
    while i < len(tokens):
        current = tokens[i]
        if current == '*':
            left = processed.pop()
            i += 1
            right = tokens[i]
            processed.append(left * right)
        else:
            processed.append(current)
        i += 1

    result = processed[0]
    for i in range(1, len(processed), 2):
        op = processed[i]
        right = processed[i+1]
        if op == '+':
            result += right
        elif op == '-':
            result -= right
    return result


if __name__ == "__main__":
    filenames = ["input01.txt", "input02.txt", "input03.txt"]
    outputnames = ["output01.txt", "output02.txt", "output03.txt"]

    for filename in filenames:
        for output in outputnames:
            with open(filename) as f_in:
                with open(output, "w") as f_out:
                    f_out.write(f"{filename}:\n")
                    for line in f_in:
                        line = line.strip()
                        if not line:
                            continue
                        tokens = line.split()
                        rationals = []
                        try:
                            for token in tokens:
                                if '/' in token:
                                    rational = Rational(token)
                                else:
                                    rational = Rational(int(token))
                                rationals.append(rational)
                            r_list = RationalList(rationals)
                            total = r_list.sum()
                            f_out.write(f"{line} = {total}\n")
                        except Exception as e:
                            f_out.write(f"Помилка у виразі '{line}': {e}\n")