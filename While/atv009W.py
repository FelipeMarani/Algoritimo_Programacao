i = 1
total = 0
while True:
    nota1 = float(input("Digite a nota do aluno {}°: ".format(i)))
    if nota1 == 999:
        break
    total += nota1 
    
    i += 1
i -= 1
med = total / i
print("Média da sala ficou em: {}".format(round(med, 2)))