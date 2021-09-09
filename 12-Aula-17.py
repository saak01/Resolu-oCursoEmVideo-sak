#testes praticos
'''
num=[2,5,9,8]
num.append(10) #forma de adicionar normal
num.insert(0,999)# insert adiciona o desejado e pode escolher a posicao
num.sort(reverse=True)#sort deixa em ordem, e com o reverse faz em ordem do maior pro menor
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''
'''
#teste2
num=[2,5,9,8]
num.append(10) #forma de adicionar normal
num.insert(0,999)# insert adiciona o desejado e pode escolher a posicao
num.pop() #pop remove a ultima posicao impressa, mas pode adicionar a posicao no parenteses.
num.remove(999)# remove funciona da mesma forma so que ao inves da posição é adicionado os itens/
#os modos de remover vao remover sempre o primeiro item desejado, se tiver mais de um, deve ser feito laços condicionais
num.del(1)
in # vai seri muito util
print(num)
print(f'Essa lista tem {len(num)} elementos.')

'''
'''
#teste 3
from typing_extensions import ParamSpec


valores = []
valores.append(3)
valores.append(6)
valores.append(9)
valores.append(12)
''
#uma opc
'''for v in valores:
    print(v)
'''
#outra opc
'''for pos in range(0,len(valores)):
    print(f'{valores[pos]}')'''
#forma interessante 
'''
for p,v in enumerate(valores):
    print(f'posicao  {p} valor {v}')'''
#teste3
'''
valores=[]
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
print(f'Sua lista é {valores}')
valores.sort()
print(f'Os valores em ordem são{valores}')
'''
#teste4
'''
a=[2,3,4,5,6]
b=a#isso é uma ligação. Se voce mexer em uma das lista vai ,exer nas duas.
b=a[:]#isso é uma copia
'''
#exercicio78
'''
listanum=[]
mai=0
men=0
for c in range (0,5):
    listanum.append(int(input(f'Digite o número desejado, ele ficara na posição{c}: ')))
    if c==0:
        mai=men= listanum[c]
    else:
        if listanum[c]>mai:
            mai=listanum[c]
        if listanum[c]<men:
            men=listanum[c]
print('=-'*30)
print(f'Os valores digitados foram: {listanum}')
print(f'\n O maior número é {mai} nas posições',end='')
for i,v in enumerate(listanum):
    if v ==mai:
        print(f': ....{i}',end='')
print(f'\n O menor número é {men} nas posições',end='')
for i,v in enumerate(listanum):
    if v ==men:
        print(f': ...{i}',end='')
'''
#exercicio79 incompleto
'''
listanum=[]
esc= ''
mai=men=veri=n=0
while True:
    n=listanum.append(int(input('Digite um valor: ')))    
    esc= str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if esc not in 'SN':
        esc= str(input('Erro, a letra digitada não condiz com as instruções: ')).upper().strip()[0]
    if esc=='S':
        print('Valor adicionado com sucesso...')
     
    if esc=='N':
        break

print(f'Os número digitados foram {listanum}')
print(f'O maior número é: {max(listanum)}')
print(f'O menor número é: {min(listanum)}')
'''

#exercicio79v2
'''
print('=-='*15)
numero=[]
while True:
    n=int(input('Digite o número desejado: '))
    if n not in numero:
        numero.append(n)
        print('Número adicionado...')
    else:       
            print('Valor duplicado! Não vou adicionar...')
            
    r=str(input('Deseja continuar?[S/N]:  ')).strip().upper()[0]
    if r == 'N':
        break
    if r not in 'SN':
        r=str(input('Erro, você digitou a letra errada, deseja continuar?[S/N]:  ')).strip().upper()[0]
numero.sort()#o sort é usado antes, na hora da impressao só é colocado o normal
print(f'Os números digitados foram: {numero}')
print(f'O maior número digitado foi: {max(numero)}')
print(f'O menor número digitado foi: {min(numero)}')
print('=-='*15)
'''

#exercicio80# #estudarmais.
'''
lista=[]
n=menor=0
print('=-='*15)
for c in range(0,5):
    n=int(input('Digite um número: '))    
    if c==0 or n>lista[-1]:
        lista.append(n)
    else:
        pos=0
        while pos < lista[-1]:
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos+=1
print('=-='*15)
print(lista)
'''
#exercicio81
'''
print('=-='*15)
numlist=[]
while True:
    n= int(input('Digite o valor desejado: '))
    numlist.append(n)    
    esc=str(input('Você deseja continuar?[S/N] ')).strip().upper()[0]
    if esc not in 'SN':
         esc=str(input('Opção inválida,você deseja continuar?[S/N] ')).strip().upper()[0]
    if esc == 'S':
        print('Número adicionado...')
    if esc =='N':
        break
print('=-='*15)
print(f'No total foram {len(numlist)} números digitados.') #nao esquecer de usar o len
numlist.sort(reverse=True)
print(f'{numlist}')
if 5 in numlist:
    print('O número 5, está na lista')
else:
    print('O número 5, não está na lista')
print('=-='*15)
'''
'''
listanum=[]
pares=[]
impar=[]
while True:
    n=int(input('Digite o valor desejado: '))
    listanum.append(n)
    esc=str(input('Você deseja continuar?[S/N] ')).upper().strip()[0]
    #verificação
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)
    
    #menu
    if esc not in 'SsNn':
        esc=str(input('Opção inválida!Você deseja continuar?[S/N] ')).upper().strip()[0]        
    if esc in 'Ss':
        print('Número adicionado com sucesso...')
    if esc in 'Nn':
        break
'''

for c in range(0,10,3):
    print (c)