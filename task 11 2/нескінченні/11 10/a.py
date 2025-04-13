def L():
    Ln = 2
    n = 0
    yield Ln, n

    while True:
        n += 1
        Ln = 4 * n + 2 + 1 / (Ln + 1)

        yield Ln, n

if __name__ == '__main__':
    for elem, num in L():
        print(f"x({num}) = {elem}")