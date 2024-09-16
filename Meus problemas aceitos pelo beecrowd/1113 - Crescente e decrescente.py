a = 0
b = 1
while a != b:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        print('Decrescente')
    elif b > a:
        print('Crescente')
