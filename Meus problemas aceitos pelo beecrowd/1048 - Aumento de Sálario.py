a = float(input())
if a >= 0 and a <= 400.00:
    soma = (a * 0.15)
    doma = a + soma
    print(f'Novo salario: {doma:.2f}')
    print(f'Reajuste ganho: {soma:.2f}')
    print('Em percentual: 15 %')
else:
    if a >= 400.01 and a <= 800.00:
        soma = (a * 0.12)
        doma = a + soma
        print(f'Novo salario: {doma:.2f}')
        print(f'Reajuste ganho: {soma:.2f}')
        print('Em percentual: 12 %')
    else:
        if a >= 800.01 and a <= 1200.00:
            soma = (a * 0.10)
            doma = a + soma
            print(f'Novo salario: {doma:.2f}')
            print(f'Reajuste ganho: {soma:.2f}')
            print('Em percentual: 10 %')
        else:
            if a >= 1200.01 and a <= 2000.00:
                soma = (a * 0.07)
                doma = a + soma
                print(f'Novo salario: {doma:.2f}')
                print(f'Reajuste ganho: {soma:.2f}')
                print('Em percentual: 7 %')
            else:
                if a >= 2000.01:
                    soma = (a * 0.04)
                    doma = a + soma
                    print(f'Novo salario: {doma:.2f}')
                    print(f'Reajuste ganho: {soma:.2f}')
                    print('Em percentual: 4 %')
