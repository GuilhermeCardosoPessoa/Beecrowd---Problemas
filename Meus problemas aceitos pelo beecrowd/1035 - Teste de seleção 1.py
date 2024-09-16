a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = c + d
f = a + b
if b > c and d > a and e > f and c > 0.0 and d > 0.0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
