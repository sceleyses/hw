from Rational import Rational

class RationalList(list):
    def __init__(self, iterable=None):
        if iterable is not None:
            iterable = self._validate(iterable)
            super().__init__(iterable)
        else:
            super().__init__()

    def _validate(self, items):
        for item in items:
            if not isinstance(item, Rational):
                raise ValueError("Елементи повинні бути типу Rational")
        return items

    def append(self, item):
        if not isinstance(item, Rational):
            raise ValueError("Елементи повинні бути типу Rational")
        super().append(item)

    def extend(self, iterable):
        iterable = self._validate(iterable)
        super().extend(iterable)

    def insert(self, index, item):
        if not isinstance(item, Rational):
            raise ValueError("Елементи повинні бути типу Rational")
        super().insert(index, item)

    def __setitem__(self, index, item):
        if not isinstance(item, Rational):
            raise ValueError("Елементи повинні бути типу Rational")
        super().__setitem__(index, item)

    def __len__(self):
        return super().__len__()

    def __str__(self):
        return f"[{', '.join(str(item) for item in self)}]"

if __name__ == '__main__':
    r1 = Rational(1, 6)
    r2 = Rational(2, 6)

    RList = RationalList([r1, r2])
    print(RList)
    print(len(RList))

    RList.append(Rational(3, 6))
    print(RList)
    print(len(RList))

    RList[0] = Rational(4, 6)
    print(RList)
    print(len(RList))

    RList.extend([Rational(5, 6)])
    print(RList)
    print(len(RList))
