x = float(input("x= "))
xk = -x
for k in range(2, 11):
    xk = -xk * (x/k)*(k - 1)
    print(xk)