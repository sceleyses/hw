def XK(n, x):
    xk = x
    yield xk, 0

    for k in range(1, n + 1):
        xk = xk * (x ** 2) / ((2 * k + 1) * 2 * k)

        yield xk, k


if __name__ == '__main__':
    x = int(input("x = "))
    n = int(input("n = "))

    for elem, num in XK(x, n):
        print(f"x({num}) = {elem}")