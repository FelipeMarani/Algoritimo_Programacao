x = int(input("Quantos alunos há na turma?: "))
for i in range(1, x+1):
    nt1 = float(input("Digite a primeira nota: "))
    nt2 = float(input("Digite a segunda nota: "))
    nt3 = float(input("Digite a terceira nota: "))
    med = (nt1 + nt2 + nt3)/3
    if med >= 6:
        print("Média: {:.1f} \nAluno Aprovado".format(med))
    else:
        print("Média: {:.1f} \nAluno Reprovado".format(med))