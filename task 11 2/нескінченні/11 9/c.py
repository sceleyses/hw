def P():
    Pn = 2/3
    n = 1
    yield Pn, n

    while True:
        n += 1
        Pn = Pn * (n + 1) / (n + 2)
        yield Pn, n

if __name__ == '__main__':
    for elem, num in P():
        print(f"x({num}) = {elem}")