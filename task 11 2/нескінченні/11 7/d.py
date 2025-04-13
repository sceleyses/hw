def XK(x):
    xk = 1
    yield xk, 0
    k = 0

    while True:
        k += 1
        xk = xk * ((x * k + x) / k ** 2)

        yield xk, k

if __name__ == '__main__':
    x = int(input("x= "))

    for elem, num in XK(x):
        print(f"x({num}) = {elem}")