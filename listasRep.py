from random import randint

# for aluno in alunos:
#    print(f'O Nome do aluno é: {aluno}')

# for aluno in alunos:
#    nota = randint(3, 10)
#    print(f'A nota do aluno {aluno} foi {nota}')

# for aluno in alunos:
#     nota_1 = randint(3, 10)
#     nota_2 = randint(4, 9)
#     nota_3 = randint(3, 7)
#
#     nota_final = nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5
#
#     print(f'A nota final do aluno {aluno} foi {nota_final}')


alunos = ['João', 'Ana', 'Clara', 'José', 'Bento']
notas = [randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10)]

for aluno, nota in zip(alunos, notas):
    print(f'A nota do {aluno} foi {nota}')