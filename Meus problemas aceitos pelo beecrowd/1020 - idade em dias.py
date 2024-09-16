a = int(input())
aoma = a // 365
b = aoma * 365
boma = a - b
coma = boma // 30
doma = coma * 30
eoma = boma - doma
foma = eoma // 1
print(f'{aoma} ano(s)')
print(f'{coma} mes(es)')
print(f'{foma} dia(s)')
