a = int(input())
b = 1
while b <= a:
    c = int(input())
    if c == 0:
        print('NULL')
        b += 1
    elif c > 0 and c % 2 == 0:
        print('EVEN POSITIVE')
        b += 1
    elif c < 0 and c % 2 == 0:
        print('EVEN NEGATIVE')
        b += 1
    elif c > 0 and c % 2 != 0:
        print('ODD POSITIVE')
        b += 1
    elif c == 0:
        print('NULL')
        b += 1
    else:
        print('ODD NEGATIVE')
        b += 1
