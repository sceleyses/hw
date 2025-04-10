Pn = 1
for n in range(2, 11):
    Pn = Pn * (1 - (1 / n**2))
    print(Pn)