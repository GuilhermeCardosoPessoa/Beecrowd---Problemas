a, b = input().split()
a = float(a)
b = float(b)
if a > 0.0 and b > 0.0:
    print('Q1')
else:
    if a < 0.0 and b > 0.0:
        print('Q2')
    else:
        if a < 0.0 and b < 0.0:
            print('Q3')
        else:
            if a > 0.0 and b < 0.0:
                print('Q4')
            else:
                if a == 0.0 and b == 0.0:
                    print('Origem')
                else:
                    if a == 0.0 and b > 0.0 or b <0.0:
                        print('Eixo Y')
                    else:
                        if b == 0.0 and a > 0.0 or a <0.0:
                            print('Eixo X')
