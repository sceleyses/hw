class Vector2D:
    def __init__(self, *v):
        if len(v) == 0:  # нульовий вектор
            self.v1 = 0.0
            self.v2 = 0.0
        elif len(v) == 1:
            if isinstance(v[0], Vector2D):
                self.v1, self.v2 = v[0].v1, v[0].v2
            else:
                self.v1, self.v2 = map(float, v[0])

        elif len(v) == 2:
            self.v1, self.v2 = map(float, v)
        else:
            raise ValueError("По таких даних неможливо створити вектор!")

    def __str__(self):
        return f"{self.v1:.2f}, {self.v2:.2f}"

if __name__ == '__main__':
    v = Vector2D(1, 2)
    print(v)