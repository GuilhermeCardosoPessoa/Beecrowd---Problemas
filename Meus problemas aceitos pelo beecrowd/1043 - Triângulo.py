a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a >= 2.01:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        soma = ((a + b) * c) / 2
        print('Area =', soma)
    else:
        soma = a + b + c
        print('Perimetro =', soma)
else:
    if a == 2 and b == 2 and c == 2:
        soma = a + b + c
        print('Perimetro =', soma)
