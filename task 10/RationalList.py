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

        validated = []
        for item in items:
            if isinstance(item, int):
                validated.append(Rational(item, 1))
            elif isinstance(item, Rational):
                validated.append(item)
            else:
                raise ValueError("Елементи повинні бути типу Rational або int")
        return validated

    def append(self, item):
        if not isinstance(item, (Rational, int)):
            raise ValueError("Елементи повинні бути типу Rational")
        if isinstance(item, int):
            item = Rational(item)
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

    def __iadd__(self, other):
        if isinstance(other, str):
            raise TypeError("Елементи повинні бути типу Rational, int або RationalList")

        try:
            iter(other)
        except TypeError:
            self.append(other)
        else:
            self.extend(other)
        return self

    def __iter__(self):
        # Створюємо звичайний список для сортування, щоб уникнути рекурсії
        elements = list(super().__iter__())
        sorted_elements = sorted(elements, key=lambda x: (-x.d, -x.n))
        return iter(sorted_elements)

    def sort_descending(self):
        super().sort(key=lambda x: (-x.d, -x.n))

    def __str__(self):
        return f"[{', '.join(str(item) for item in self)}]"


if __name__ == "__main__":
    r_list = RationalList()
    r_list.append(Rational(2))
    r_list.append(Rational(3))
    r_list.append(Rational(1))

    print("До сортування:", r_list)

    r_list.sort_descending()
    print("Після сортування:", r_list)  # [2/1, 3/2, 1/2] (спадання знаменників, потім чисельників)

