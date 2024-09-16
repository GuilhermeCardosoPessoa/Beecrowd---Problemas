a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a > b and a > c:
    print(f'{a:.0f} eh o maior')
if b > a and b > c:
    print(f'{b:.0f} eh o maior')
if c > b and c > a:
    print(f'{c:.0f} eh o maior')
if a == b and a == c:
    print(f'{a:.0f} eh o maior')
if b == a and b > c:
    print(f'{a:.0f} eh o maior')
if b == c and b > a:
    print(f'{b:.0f} eh o maior')
