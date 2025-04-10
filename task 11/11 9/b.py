import math

Pn = 3
for n in range(2, 11):
    Pn = Pn * (2 + (1/math.factorial(n)))
    print(Pn)