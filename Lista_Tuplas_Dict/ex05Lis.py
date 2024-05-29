lisA = []
lisB = []
cont = 0
while cont <= 0:
    x = int(input('Digite um número maior que zero para adiciona a Lista A: '))
    if x > 0:
        lisA.append(int(x))
    else:
        cont += 1
while True:
    x = int(input('Digite um número maior que zero para adicionar a lista B: '))
    if x > 0:
        lisB.append(int(x))
    else: 
        print(set(lisA) & set(lisB))
        break