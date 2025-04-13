def S(k):
    Sn = 1
    yield Sn, 1

    for n in range(2, k + 1):
        Sn = -Sn * (n / (n - 1))

        yield Sn, n

if __name__ == '__main__':
    k = int(input("k = "))

    for elem, num in S(k):
        print(f"x({num}) = {elem}")