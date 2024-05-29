nAlunos = int(input('Digite quantos alunos vc deseja calcular: '))
i = 1
while i <= nAlunos:
    name = str("Digite o nome do Aluno a ser avaliado: ")
    nota1, nota2 = map(float, input("Digite a nota do aluno {} 1 e 2 em sequência: ".format(name)).split())
    med = (nota1 + nota2) / 2
    i += 1
    if med >= 6:
        print('O aluno {} Aprovado com média {}'.format(name, med))
    else:
        print("O aluno {} reprovado com média de {}".format(name, med))
