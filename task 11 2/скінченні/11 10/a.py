def L(k):
    Ln = 2
    yield Ln, 0

    for n in range(1, k+1):
        Ln = 4 * n + 2 + 1 / (Ln + 1)

        yield Ln, n

if __name__ == '__main__':
    k = int(input("k = "))
    for elem, num in L(k):
        print(f"x({num}) = {elem}")