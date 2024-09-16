a = int(input())
aoma = a // 100
boma = aoma * 100
zoma = a - boma
coma = zoma // 50
doma = coma * 50
xoma = zoma - doma
eoma = xoma // 20
foma = eoma * 20
yoma = xoma - foma
goma = yoma // 10
homa = goma * 10
woma = yoma - homa
ioma = woma // 5
joma = ioma * 5
toma = woma - joma
koma = toma // 2
loma = koma * 2
poma = toma - loma
moma = poma // 1

print(a)
print(f'{aoma} nota(s) de R$ 100,00')
print(f'{coma} nota(s) de R$ 50,00')
print(f'{eoma} nota(s) de R$ 20,00')
print(f'{goma} nota(s) de R$ 10,00')
print(f'{ioma} nota(s) de R$ 5,00')
print(f'{koma} nota(s) de R$ 2,00')
print(f'{moma} nota(s) de R$ 1,00')
