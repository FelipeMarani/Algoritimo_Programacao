sm = 0
sd = 0
medMassa = 0
medIdade = 0
mpeso = 0
midade = 0
for c in range(3):
    for a in range(3):
        massa = float(input("Digite seu peso: "))
        sm += massa
        idade = int(input("Digite sua idade:  "))
        sd += sd
        if c == 0:
            mpeso += massa
            midade += idade
        elif c == 1:
            mpeso += massa
            midade += idade
        elif c == 3:
            mpeso += massa
            midade += idade
medMassa += sm/9
medIdade += medIdade/9
print()
print("Idade tem média de : {}".format(medIdade))
print("Massa dos atlétas tem média de : {}".format(medMassa))