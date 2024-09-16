X = int(input())
Y = int(input())

soma = 0

if X > Y:
    X, Y = Y, X

for num in range(X+1, Y):
    if num % 2 != 0:
        soma += num

print(soma)
