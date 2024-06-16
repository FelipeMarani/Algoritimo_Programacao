mtr = [ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
for l in range(0, 4):
    for c in range(0, 3):
        mtr[l][c]=int(input("Digite um valor para [{}, {}]: ".format(l, c)))
for l in range(4):
	for c in range(3):
		print(f'[{mtr[l][c]:^5}]', end='')
	print()