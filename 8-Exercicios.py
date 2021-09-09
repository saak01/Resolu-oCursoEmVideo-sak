'''from time import sleep
c=1
while c < 20:   
    print(c)
    c = c+1
    sleep(0.3)
print('Fim')'''


#exerciciosdepraticaAula14
'''from time import sleep
c=1
while c < 10:   
    print(c)
    c = c+1
    sleep(0.6)
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite o valor: '))
    r = str(input('Quer Continuar: S/N: ')).upper()
print('Fim dodoi')'''

'''par = 0
impar = 0
n = 1 
while n!=0:
    n= int(input('Digite o valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Voce digitou {} pares e {} impares'.format(par,impar))'''

#exercicio57
'''sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))'''

#exercicio58
'''from random import randint
computador = randint(1,10)
acertou = False
palpites = 0
print('----------Jogos de Adivinhação----------')
print('Escolha um número de 1 a 10 e veja se acertou :) ')
while not acertou: 
    jogador = int(input('Digite o número número que você acha que estou pensando:'))
    palpites += 1
    if jogador == computador:
        acertou = True
        print('Voce acertou com {} palpites'.format(palpites))
    else: 
        if jogador < computador:
            print('Mais')
        elif jogador > computador:
            print('Menos')      
print(computador)'''

#exercicio59
'''#menuvalores
from time import perf_counter, sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float (input('Digite o segundo número: '))
esc = 0
while esc != 5 :
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    esc = int(input('Escolha a opção que você deseja: '))    
    if esc == 1:
        n1+n2
        sleep(0.5)
        print ('A soma dos valores é {} + {} = {}'.format(n1,n2,n1+n2))
    elif esc == 2:
        n1 * n2
        print ('A multiplicação de {} X {} = {}'.format(n1,n2,n1*n2))
    elif esc == 3:
        if n1 > n2:
            print ('O {} é o maior'.format(n1))
        else:
            print('O {} é o maior '.format(n2))
    elif esc == 4:
        print('Você desejou escolher novos números, por favor redigitios: ')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float (input('Digite o segundo número: '))
    elif esc ==5:
        print('Programa encerrado')
        break
        '''
#exercicio60
'''print('Calculador de fatorial')
n = int(input('Digite o o número desejado: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end=' ')
    print('x'if c > 1 else '=',end=' ')
    f = f*c
    c -= 1
print('{}'.format(f))'''

'''#exercicio61
#progressãoaritmética
print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razao = int (input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print ('{} →'.format(termo),end='')
    termo += razao
    cont +=1'''

'''#exercicio62
#progressãoaritmética
print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razao = int (input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print ('{} →'.format(termo),end='')
    termo += razao
    cont +=1'''

#exercicio63

'''cont=0
num= 0
soma = 0
while num != 999:
    num = int(input('Digite o valor desejado: [999 para parar]'))
    soma = soma + num
    cont += 1
print('A soma de {} valores, tem o total é {}'.format(cont-1,soma-999))'''

#exercicio64
'''print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n=int(input('Quantos termos voce deseja:'))
t1 = 0
t2= 1
print('~'*30)
print('{}→{}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1+t2
    cont+=1
    t1 = t2
    t2 = t3
    print('→{}'.format(t3),end='')'''

#exercicio65
média=0
cont = 0
soma = 0
resp = 'S'
maior=0
menor =0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma+=num
    cont+=1
    if cont == 1:
        maior=menor=num
    else:
        if  num > maior:
            maior=num
        if num < menor:
            menor=num
    resp=str(input('Deseja continuar?  [S/N]'))
média = soma/cont
print('A média dos {} números impressos é:{:.2f}'.format(cont,média))
print('O maior número é: {} menor número é: {}'.format(maior,menor))