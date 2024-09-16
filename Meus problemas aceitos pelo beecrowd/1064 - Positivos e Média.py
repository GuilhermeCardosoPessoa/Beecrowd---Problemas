a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
aoma = 0
boma = 0
coma = 0
doma = 0
eoma = 0
foma = 0
homa = 0
ioma = 0
joma = 0
koma = 0
loma = 0
moma = 0
if a > 0.0:
    aoma = 0 + 1
    homa = 0 + a
if b > 0.0:
    boma = 0 + 1
    ioma = 0 + b
if c > 0.0:
    coma = 0 + 1
    joma = 0 + c
if d > 0.0:
    doma = 0 + 1
    koma = 0 + d
if e > 0.0:
    eoma = 0 + 1
    loma = 0 + e
if f > 0.0:
    foma = 0 + 1
    moma = 0 + f
soma = aoma + boma + coma + doma + eoma + foma
print(f'{soma} valores positivos')
goma = (homa + ioma + joma + koma + loma + moma) / soma
print(f'{goma:.1f}')
