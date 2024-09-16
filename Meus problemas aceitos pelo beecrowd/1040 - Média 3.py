a, b, c ,d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
soma = ((a * 2)+(b * 3)+(c * 4)+(d * 1)) / 10
if soma >= 7.0:
    print(f'Media: {soma:.1f}')
    print('Aluno aprovado.')
elif soma >= 5.0:
    e = float(input())
    doma = (soma + e) / 2
    if doma >= 5.0:
        print(f'Media: {soma:.1f}')
        print('Aluno em exame.')
        print('Nota do exame:', e)
        print('Aluno aprovado.')
        print(f'Media final: {doma:.1f}')
    else:
        if doma <= 4.9:
            print(f'Media: {soma:.1f}')
            print('Aluno em exame.')
            print('Nota do exame:', e)
            print('Aluno reprovado.')
            print(f'Media final: {doma:.1f}')
else:
    if soma <= 4.9:
        print(f'Media: {soma:.1f}')
        print('Aluno reprovado.')
