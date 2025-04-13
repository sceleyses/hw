def XK(x):
    xk = 1
    k = 0
    yield xk, 0

    while True:
        k += 1
        xk = - (xk * (k + 1) * (k + 2)) / x

        yield xk, k

if __name__ == '__main__':
    x = float(input("x = "))

    for elem, num in XK(x):
        print(f"x({num}) = {elem}")