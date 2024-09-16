a = float(input())
b = 3000
c = 4500
if a >= 0 and a<= 2000.00:
    print('Isento')
if a >= 2000.01 and a <= 3000.00:
    soma = ((a - 2000)* 0.08)
    print(f'R$ {soma:.2f}')
if a >= 3000.01 and a <= 4500.00:
    soma = ((b - 2000)* 0.08)
    doma = ((a - 3000)* 0.18)
    zoma = soma + doma
    print(f'R$ {zoma:.2f}')
if a >= 4500.01:
    soma = ((b - 2000)* 0.08)
    doma = ((c - 3000)* 0.18)
    coma = ((a - 4500)* 0.28)
    zoma = soma + doma + coma
    print(f'R$ {zoma:.2f}')
