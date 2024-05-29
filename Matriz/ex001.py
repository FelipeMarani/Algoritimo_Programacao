mtr = [ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
for l in range(0, 4):
    for c in range(0, 3):
        mtr[l][c]=int(input("Digite um valor para [{}, {}]: ".format(l, c)))
print(mtr[0])
print(mtr[1])
print(mtr[2])
print(mtr[3])