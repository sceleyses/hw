import math

def P(k):
    Pn = 3
    yield Pn, 1

    for n in range(2, k+1):
        Pn = Pn * (2 + (1 / math.factorial(n)))

        yield Pn, n

if __name__ == '__main__':
    k = int(input("k = "))
    for elem, num in P(k):
        print(f"x({num}) = {elem}")