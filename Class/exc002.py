class Aluno:
    nome = str
    cpf = str
    nt1 = float
    nt2 = float

al = Aluno()
al.nome = str(input("Digite o Nome do aluno: "))
al.cpf = str(input("Digite o Cpf do aluno: "))
al.nt1 = float(input("Digite a Nota 1° do aluno: "))
al.nt2 = float(input("Digite a Nota 2° do aluno: "))

med = (al.nt1 + al.nt2)/2
if med >= 6:
    print("Aluno aprovado com média de : {:.2f}".format(med))
else:
    print("Aluno reprovado com média de : {:.2f}".format(med))