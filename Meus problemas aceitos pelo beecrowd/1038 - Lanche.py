a, b = input().split()
a = int(a)
b = int(b)
if a == 1:
    a = 4.00
    soma = a * b
    print(f'Total: R$ {soma:.2f}')
else:
    if a == 2:
        a = 4.50
        soma = a * b
        print(f'Total: R$ {soma:.2f}')
    else:
        if a == 3:
            a = 5.00
            soma = a * b
            print(f'Total: R$ {soma:.2f}')
        else:
            if a == 4:
                a = 2.00
                soma = a * b
                print(f'Total: R$ {soma:.2f}')
            else:
                if a == 5:
                    a = 1.50
                    soma = a * b
                    print(f'Total: R$ {soma:.2f}')
