def S():
    Sn = 1
    yield Sn, 1
    n = 1

    while True:
        n += 1
        Sn = -Sn * (n / (n - 1))

        yield Sn, n

if __name__ == '__main__':

    for elem, num in S():
        print(f"x({num}) = {elem}")