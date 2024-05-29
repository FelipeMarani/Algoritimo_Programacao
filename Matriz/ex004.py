import random
def matrizINT(mtrz):
    mIT = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    lis = []
    for l in range(3):
        for c in range(3):
            valor = random.randrange(-50, 50)
            lis.append(int(valor))
            mIT[l][c] = valor
    M = max(lis)
    m = min(lis)
    return (mIT, M, m)
Matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l][c]=int(input("Digite um valor para [{}, {}]: ".format(l, c)))
print(matrizINT(mtrz=0))
print(Matriz[0])
print(Matriz[1])
print(Matriz[2])