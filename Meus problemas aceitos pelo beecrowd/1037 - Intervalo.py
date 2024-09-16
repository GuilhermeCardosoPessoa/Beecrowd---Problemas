a = float(input())
if a < 0:
    print('Fora de intervalo')
else:
    if a <= 25.00:
        print('Intervalo [0,25]')
    else:
        if a <= 50.00:
            print('Intervalo (25,50]')
        else:
            if a <= 75.00:
                print('Intervalo (50,75]')
            else:
                if a <= 100.00:
                    print('Intervalo (75,100]')
                else:
                    print('Fora de intervalo')
