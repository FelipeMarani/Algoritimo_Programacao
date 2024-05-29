lis = []
while True:
    x = int(input('Digite um número maior que 0 ou menor que 0 para encerrar o programa: '))
    if x >= 0:
        lis.append(int(x))
        lis.sort()
    else:
        lis.sort()
        print('O menor número digitado foi {}'.format(lis[0]))
        break