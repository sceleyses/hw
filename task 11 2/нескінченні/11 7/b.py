def XK(x):
    xk = -x
    yield xk, 1
    k = 1

    while True:
        k += 1
        xk = -xk * (x / k) * (k - 1)

        yield xk, k

if __name__ == '__main__':
    x = float(input("x = "))

    for elem, num in XK(x):

        print(f"x({num}) = {elem}")
