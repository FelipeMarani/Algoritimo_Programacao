x = int(input('Digite um número inteiro positivo: '))
y = int(input('Digite um número inteiro postivo: '))
j = x
if y > 0:
    for i in range(1, y):
        soma = 0
        for n in range(1, x):
            soma += x
            x = soma
        print(x)