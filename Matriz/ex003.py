matrizA = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
matrizB = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for l in range(3):
    for c in range(3):
        matrizA[l][c] = int(input("Digite um numero para adicionar a matriz A [{} linha]: ".format(l)))
for l in range(3):
    for c in range(3):
        matrizB[l][c] = int(input("Digite um numero para adicionar a matriz B [{} linha]: ".format(l)))

def soma(matrizA, matrizB):
    SMMtriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for l in range(3):
        for c in range(3):
            soma = matrizA[l][c] + matrizB[l][c]
            SMMtriz[l][c] = soma
    return SMMtriz
print(soma(matrizA, matrizB))
