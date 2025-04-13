def XK(x, n):
    xk = 1
    yield xk, 0

    for k in range(1, n+1):
        xk = xk * ((x * k + x) / k ** 2)

        yield xk, k

if __name__ =='__main__':
    x = float(input("x = "))
    n = int(input("n = "))

    for elem, num in XK(x, n):
        print(f"x({num}) = {elem}")