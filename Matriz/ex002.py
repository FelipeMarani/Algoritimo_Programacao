def matriz(trz):
    mtr = [ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
    for l in range(4):
        for c in range(3):
            mtr[l][c] = int(trz)
    print(mtr)
    return mtr

matriz(int(input("digite um numero: ")))