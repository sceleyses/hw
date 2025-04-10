import math
xk = 1
x = int(input())
for k in range(1, 11):
    xk = xk * (math.factorial(x*(k*2-k)))/math.factorial(k**2 + k)
    print(xk)