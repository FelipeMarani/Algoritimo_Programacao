x = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, x +1):
    if x % i == 0:
        soma += 1 
print(soma)