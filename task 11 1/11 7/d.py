xk = 1
x = int(input("x= "))
for k in range(1, 11):
    xk = xk * ((x * k + x)/ k**2)
    print(xk)