noivo = set()
noiva = set()

entrada = input()
 
while entrada != 'ACABOU':
    convidado, anfitriao = entrada.split(';')
    if anfitriao == 'noivo':
        noivo.add(convidado)
    else:
        noiva.add(convidado)
    entrada = input()
 
final = sorted(noivo | noiva)
apenas_noiva = sorted(noiva - noivo)
apenas_noivo = sorted(noivo - noiva)
ambos = sorted(noivo & noiva)
apenas_um = sorted(noivo ^ noiva)

print('-' * 20)
print('LISTA FINAL')
print('-' * 20)
for convidado in final:
    print(convidado)
print()
 
print('-' * 20)
print('APENAS NOIVA')
print('-' * 20)
for convidado in apenas_noiva:
    print(convidado)
print()
 
print('-' * 20)
print('APENAS NOIVO')
print('-' * 20)
for convidado in apenas_noivo:
    print(convidado)
print()
 
print('-' * 20)
print('POR AMBOS')
print('-' * 20)
for convidado in ambos:
    print(convidado)
print()
 
print('-' * 20)
print('POR APENAS UM DELES')
print('-' * 20)
for convidado in apenas_um:
    print(convidado)
