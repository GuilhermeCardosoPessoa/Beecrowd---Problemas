a, b = input().split()
a = int(a)
b = int(b)
if a == b:
    print('O JOGO DUROU 24 HORA(S)')
else:
    if a < b:
        soma = b - a
        print(f'O JOGO DUROU {soma} HORA(S)')
    else:
        if a > b:
            b += 24
            soma = b - a
            print(f'O JOGO DUROU {soma} HORA(S)')
