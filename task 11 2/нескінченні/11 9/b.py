import math

def P():
    Pn = 3
    n = 1
    yield Pn, n

    while True:
        n += 1
        Pn = Pn * (2 + (1 / math.factorial(n)))

        yield Pn, n

if __name__ == '__main__':
    for elem, num in P():
        print(f"x({num}) = {elem}")