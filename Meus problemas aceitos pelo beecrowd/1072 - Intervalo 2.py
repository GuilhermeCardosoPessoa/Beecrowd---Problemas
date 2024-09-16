a = int(input())
b = 1
soma = 0
doma = 0
while b <= a:
    c = int(input())
    if c >= 10 and c <= 20:
        soma += 1
        b += 1
    else:
        doma += 1
        b += 1
print(f'{soma} in')
print(f'{doma} out')
