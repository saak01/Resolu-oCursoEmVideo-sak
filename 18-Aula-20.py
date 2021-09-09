'''
#funcao 
def titulo(txt):
    print('=-='*30)
    print(txt)
    print('=-='*30)


titulo('Joao é pika')
titulo('A mina tem mo fundao')
'''
'''
a=4
b=5
s=a+b
print(s)
a=8
b=9
s=a+b
print(s)
a=4
b=3
s=a+b
print(s)
'''
'''
def soma(a,b):
    s=a+b
    print(s)


soma(4,5)
soma(5,5)
soma(3,5)
'''
'''
valor=[1,2,3,4,5]#lista
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *=2
        pos+=1


valor=[1,2,3,4,5]
dobra(valor)
print(valor)

'''

'''
def soma(a,b):
    print(f'A={a} e B={b}')
    s=a+b
    print(f'{a}+{b}={s}')


soma(1,4)
'''

#exercicio96

'''
def area(a,b):
    ar=a*b
    print(f'O terreno com {a }x {b} é de {ar:.2f} m²')

print('Controle de Terreno')
print('---'*15)
area(a=float(input('Largura (m): ')),b=float(input('Comprimento (m): ')))
'''
'''
#exercicio96Guanabara
def area(larg,comp):
    a = larg * comp
    print(f'O terreno com {larg}x {comp} é de {a:.2f} m²')


print('Controle dos Terrenos')
print('--'*20)
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
area(l,c)
'''
#exercicio97
'''
def escreva(msg):
    tot=len(msg)
    print('='*tot)
    print(msg)
    print('='*tot)


#principal
escreva(str(input('Digite o valor: ')))
'''

'''
#exercicio98

from os import EX_NOTFOUND


def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if  i<f:
        cont=i
        while cont<=f:
            print(f'{cont}',end='')
            cont+=1
        print('  Fim')
    else:
        cont=i
        while cont >= f:
            print(cont)
            cont -= p
        print('Fim')

#funcaoprimaria
contador(1,10,1,  )
contador(10,0,2)
contador(int(input('Primeiro')),int(input('Primeiro')),int(input('Primeiro')))
'''
'''
from time import sleep

def maior(* num):
    cont=ma=0
    print('\n Analisandos os valores')
    for valor in num:
        print(f'{valor}',end=' ',flush=True )
        sleep(0.3)
        if cont==0:
            ma=valor
        else:
            if valor>ma:
                ma=valor
        cont+=1
    print(f'\n{ma}')


#programaPrincipal
maior(1,7,4,5)
maior(1,322,4)
maior(0)
'''
'''
def maior(*num):
    ma=cont=0
    print('\nValores inseridos foram:')
    for valor in num:
        print(f'{valor}',end=',')
        if cont ==0:
            ma=valor
        else:
            if valor>ma:
                ma=valor
        cont+=1
    print(f'\nO maior número é:{ma}')
        



maior(0,4,3,22,1,20)
maior(4,3,77,211,2)
'''

from random import randint

def sorteia(lista):
    for cont in range (0,5):
        lista.appende

numeros=[]
sorteia(numeros)
print(numeros)