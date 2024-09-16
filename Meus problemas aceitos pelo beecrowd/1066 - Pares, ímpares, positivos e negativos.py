b = 0
c = 0
d = 0
e = 0
x = 0
while x <= 4:
    try:
        a = int(input())
        x +=1
        if a > 0:
            d += 1
            if a % 2 == 1:
                c += 1
            else:
                b +=1
        elif a == 0:
            if a % 2 == 1:
                c += 1
            else:
                b +=1
        else:
            e =+ 1
            if a % 2 == 1:
                c += 1
            else:
                b +=1
    except EOFError:
        break
print(f'{b} valor(es) par(es)')
print(f'{c} valor(es) impar(es)')
print(f'{d} valor(es) positivo(s)')
print(f'{e} valor(es) negativo(s)')
