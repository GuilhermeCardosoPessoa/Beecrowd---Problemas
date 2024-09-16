a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a > b and b > c:
    print(c)
    print(b)
    print(a)
    print()
    print(a)
    print(b)
    print(c)
else:
    if c > a and a > b:
        print(b)
        print(a)
        print(c)
        print()
        print(a)
        print(b)
        print(c)
    else:
        if b > a and a > c:
            print(c)
            print(a)
            print(b)
            print()
            print(a)
            print(b)
            print(c)
        else:
            if a > c and c > b:
                print(b)
                print(c)
                print(a)
                print()
                print(a)
                print(b)
                print(c)
            else:
                if c > b and b > a:
                    print(a)
                    print(b)
                    print(c)
                    print()
                    print(a)
                    print(b)
                    print(c)
                else:
                    if b > c and c > a:
                        print(a)
                        print(c)
                        print(b)
                        print()
                        print(a)
                        print(b)
                        print(c)
