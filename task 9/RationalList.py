from Rational import Rational

class RationalList(list):
    def __init__(self, iterable=None):
        if iterable is not None:
            iterable = self._validate(iterable)
            super().__init__(iterable)
        else:
            super().__init__()

    def _validate(self, items):
        if not isinstance(items, (list, RationalList)):
            items = [items]

        for item in items:
            if not isinstance(item, (Rational, int)):
                raise ValueError("Елементи повинні бути типу Rational")

            if isinstance(item, int):
                return Rational(item)
        return items

    def append(self, item):
        if not isinstance(item, (Rational, int)):
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


    def __add__(self, other):
        if isinstance(other, (Rational)):
            other = self._validate(other)
            return RationalList(super().__add__(other))

        if isinstance(other, (int)):
            other = self._validate(Rational(other))
            return RationalList(super().__add__(other))

        if isinstance(other, (RationalList)):
            other = self._validate(other)
            return RationalList(super().__add__(other))


    def __str__(self):
        return f"[{', '.join(str(item) for item in self)}]"

if __name__ == '__main__':
    r1 = Rational(1, 6)
    r2 = Rational(2, 6)

    RList = RationalList([r1, r2])
    print(RList)
    print(len(RList))

    # RList.append(Rational(3, 6))
    # print(RList)
    # print(len(RList))
    #
    # RList[0] = Rational(4, 6)
    # print(RList)
    # print(len(RList))
    #
    # RList.extend([Rational(5, 6)])
    # print(RList)
    # print(len(RList))

    add1 = RList + RList
    add2 = RList + r1
    add3 = RList + 2
    print(add1, add2, add3)
    print(len(add1))

