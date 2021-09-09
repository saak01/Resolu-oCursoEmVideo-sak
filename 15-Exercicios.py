#Exericios84
'''

print('=-='*15)
temp=[]
principal=list()
cont=maior=men=0
while True:    
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))    
    if len(principal) ==0:
        maior=men=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<men:
            men=temp[1]
    principal.append(temp[:])
    temp.clear()#clear serve para não repetir a lista varias vezes.

    esc= str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if esc == 'N':
        break

print(f'O número de pessoas cadastradas foi {len(principal)}')
print(f'O maior peso é de {maior}')
for p in principal:
    if p[1] == maior:
        print(f'\nOs nome dos mais pesados são: {p[0]} com o peso de {maior}',end=' ')
    if p[1] == men:
        print(f'\n Os nomes dos mais leves são : {p[0]} com o peso de {men}',end=' ')
print('=-='*15)

'''

#exercicio85#minhaversão
'''
print('=-='*15)
temp = []
num=[]
pares=[]
impares=[]
for c in range(1,8):
    temp.append(int(input(f'Digite o {c} número desejado: ')))
    num.append(temp[:])
    temp.clear()
for p in num:
    if p[0] % 2 == 0:
        pares.append(p[0])
    else:
        impares.append(p[0])
print('=-='*15)
print(f'Os números pares são {sorted(pares)}')
print(f'Os números impares são {sorted(impares)}')
'''
#exercicio85v2

'''
num=[[],[]]
valor=0
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor desejado: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os número pares são {num[0]}')
print(f'Os números impares {num[1]}')
'''
#exercicios86
'''
matriz=[[0,0,0],[0,0,0],[0,0,0,]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]=int(input(f'Digite um valor:[{l},{c}] '))
print('=-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5#centralizar pra arrumar}]',end='')
    print()
    '''
#exercicio87
'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=[]
impares=[]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor: [{l},{c}] '))
print('=-'*20)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar+=matriz[l][c]
        
    print()

  '''      
'''
print(f'Soma dos números pares é: {spar}')
for l in range (0,3):
        scol+= matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for c in range(0,3):
    if c ==0:
        mai=matriz[1][c]
    elif matriz[1][c]>mai:
        mai=matriz[1][c]
print(f'O maior valor da segunda linha {mai}')
'''
    

 #exercicio88
'''
from time import sleep
from random import randint
num=[]
print('=-='*15)
print('Palpites para a Mega Sena')
print('=-='*15)
esc=int(input('Digite quantos jogos você deseja: '))
for c in range (0,esc):
    num=[[randint(1,61)],[randint(1,61)],[randint(1,61)],[randint(1,61)],[randint(1,61)],[randint(1,61)]]   
    print(f'O {c+1} jogo é: {num}')
    sleep(0.5)
    '''

#exercicio88 pelo guanabara
'''
from random import randint
print('-=-'*15)
lista = list()
cont = 0
while True:
    num=randint(1,60)
    if num not in lista:
        lista.append(num)
        cont += 1
        if cont >=6:
            break
lista.sort()
print(f'Os números sorteados foram {lista}')

'''

'''
ficha = []
while True:
    nome = str(input('Digite o seu nome: '))
    nota1=float(input('Digite a sua primeira nota: '))
    nota2=float(input('Digita a sua segunda nota: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('=-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('---'*20)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>}')
while True:
    opc=int(input('Mostra a nota de qual aluno?[999 interrompe]: '))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

'''
