import random
r = random.randint(1, 100)
tt = 1
n = 0
while n != r:
    n = int(input('Digite um valor de 1 a 100: '))
    if n < r:
        print('Tente um numero maior')
        tt = tt+1
    elif n > r:
        print('Tente um número menor')
        tt = tt+1
    else:
        print('Parabéns! Você adivinhou corretamente em {} tentativas.'.format(tt))
        break
