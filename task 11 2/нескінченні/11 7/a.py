def XK(x):
    xk = x
    k = 0
    yield xk, 0

    while True:
        k += 1
        xk = xk * (x ** 2) / ((2 * k + 1) * 2 * k)

        yield xk, k

if __name__ == '__main__':
    x = float(input("x= "))

    for elem, num in XK(x):

        print(f"x({num}) = {elem}")
