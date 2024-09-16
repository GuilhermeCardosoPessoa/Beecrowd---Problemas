a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
soma = a**2
doma = b**2
loma = c**2
if a >= b and a >= c:
    if b + c <= a:
        print('NAO FORMA TRIANGULO')
    else:
        if soma == doma + loma:
                print('TRIANGULO RETANGULO')
        if soma > doma + loma:
                print('TRIANGULO OBTUSANGULO')
        if soma < doma + loma:
                print('TRIANGULO ACUTANGULO')
        if a == b and a == c and b == c:
                print('TRIANGULO EQUILATERO')
        if a == b  and a != c or c == b  and c != a or c == a and c != b:
                print('TRIANGULO ISOSCELES')
elif b >= a and b >= c:
    if a + c <= b:
        print('NAO FORMA TRIANGULO')
    else:
        if doma == soma + loma:
                print('TRIANGULO RETANGULO')
        if doma > soma + loma:
                print('TRIANGULO OBTUSANGULO')
        if doma < soma + loma:
                print('TRIANGULO ACUTANGULO')
        if a == b and a == c and b == c:
                print('TRIANGULO EQUILATERO')
        if a == b  and a != c or c == b  and c != a or c == a and c != b:
                print('TRIANGULO ISOSCELES')
elif c >= b and c >= a:
    if b + a <= c:
        print('NAO FORMA TRIANGULO')
    else:
        if loma == doma + soma:
                print('TRIANGULO RETANGULO')
        if loma > doma + soma:
                print('TRIANGULO OBTUSANGULO')
        if loma < doma + soma:
                print('TRIANGULO ACUTANGULO')
        if a == b and a == c and b == c:
                print('TRIANGULO EQUILATERO')
        if a == b  and a != c or c == b  and c != a or c == a and c != b:
                print('TRIANGULO ISOSCELES')
elif a == b and b == c:
    if b + a <= c:
        print('NAO FORMA TRIANGULO')
    else:
        if loma == doma + soma:
                print('TRIANGULO RETANGULO')
        if loma > doma + soma:
                print('TRIANGULO OBTUSANGULO')
        if loma < doma + soma:
                print('TRIANGULO ACUTANGULO')
        if a == b and a == c and b == c:
                print('TRIANGULO EQUILATERO')
        if a == b  and a != c or c == b  and c != a or c == a and c != b:
                print('TRIANGULO ISOSCELES')
