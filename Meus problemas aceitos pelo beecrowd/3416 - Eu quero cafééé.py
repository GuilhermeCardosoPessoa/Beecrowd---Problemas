from math import ceil
 
N, L, D = input().split()
N = int(N)
L = int(L)
D = int(D)
 
necessario = (N * D) / 1000
minimo = ceil(necessario / L) * L
 
print(minimo)
