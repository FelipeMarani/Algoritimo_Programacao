matrizA = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
for l in range(0, 4):
    for c in range(0, 4):
        matrizA[l][c]=int(input("Digite um valor para [{}, {}]: ".format(l, c)))
matrizB = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
for l in range(0, 4):
    for c in range(0, 4):
        matrizB[l][c]=int(input("Digite um valor para [{}, {}]: ".format(l, c)))

def multMatriz(matrizA, matrizB):
    MatrizF = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for l in range(0, 4):
        for c in range(0, 4):
           MatrizF[l][c] = matrizA[l][c] * matrizB[l][c] 
    return MatrizF
print(multMatriz(matrizA, matrizB))
