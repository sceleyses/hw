x = float(input("x= "))
xk = x
for k in range(1, 11):
    xk = xk * (x**2)/((2*k+1)*2*k)
    print(xk)