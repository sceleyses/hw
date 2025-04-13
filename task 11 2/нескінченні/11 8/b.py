def S():
    Sn = 1 / 2
    yield Sn, 0
    n = 2

    while True:
        n += 1
        Sn = -Sn + 1 / ((n - 1) * n)

        yield Sn, n

if __name__ == '__main__':

    for elem, num in S():
        print(f"x({num}) = {elem}")