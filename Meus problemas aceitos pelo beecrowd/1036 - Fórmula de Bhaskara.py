a , b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
doma = a + b + c
if doma % 2 == 0.00 or doma % 2 == 1.00:
    print('Impossivel calcular')
else:
    delta = (b**2) - 4 * a * c
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
