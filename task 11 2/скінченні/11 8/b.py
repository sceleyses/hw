def S(k):
    Sn = 1 / 2
    yield Sn, 0

    for n in range(3, k+1):
        Sn = -Sn + 1 / ((n - 1) * n)
        yield Sn, n

if __name__ == '__main__':
    k = int(input("k = "))

    for elem, num in S(k):
        print(f"x({num}) = {elem}")