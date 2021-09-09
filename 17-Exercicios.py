#exercicio89
'''
galera={'Nome':str(input('Digite o seu nome: ')),'Media':float(input('Digite sua média.'))}
print('=-='*15)
print(f'O {galera["Nome"]} é igual o nome.')
print(f'A {galera["Media"]} é igual a média')
if galera['Media']>=7:
    galera['Situação']='Aprovado'
elif galera['Media']>=5:
    galera['Situação']='Recuperação'
elif galera['Media']<5:
    galera['Situação']='Reprovado'
for k,v in galera.items():
    print(f'-{k} é igual a {v}')

    '''
#exercicio90
'''
from time import sleep
from random import randint
from operator import itemgetter
jogo= {'jogador1': randint(1,6),
'jogador2': randint(1,6),
'jogador3': randint(1,6),
'jogador4': randint(1,6)}
ranking=list()

for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('===RANKING===')
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')

    '''
#exercicio91
'''
from datetime import date
atual = date.today().year
cadastro={'Nome':str(input('Nome: ')),
'Data':int(input('Digite o ano de nascimento: '))
,'Ctps':int(input('Carteira de Trabalho(0 não tem): '))}
cadastro['Idade']=atual-cadastro['Data'] #assim que se adiciona mais coisas num dicionario
if cadastro['Ctps']!=0:
    cadastro['Contratação']=int(input('Digite o ano de contratação: '))
    cadastro['Salário']=float(input('Por favor, informe seu salário: '))
    cont= (35-(atual - cadastro['Contratação']))
    aposent=cont+cadastro['Idade']
    cadastro['Aposentadoria']=aposent
print('---'*20)
cadastro['Idade']=atual-cadastro['Data'] #assim que se adiciona mais coisas num dicionario
for k,v in cadastro.items():
    print(f'{"-":<5}{k} tem o valor de {v}')
'''

#exercicio92
'''
from datetime import date
print('---'*15)
atual= date.today().year
cadastro={}
nome=str(input('Digite seu nome: '))
cadastro['Nome']=nome
ano= int(input('Ano de nascimento: '))
idade=atual-ano
cadastro['Idade']=idade
cadastro['Cpts']=int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['Cpts']!=0:
    cont=int(input('Ano de contratação: '))
    cadastro['Contratação']=cont
    cadastro['Salário']=int(input('Salário: '))
    aposent=(35-(atual-cont))+idade
    cadastro['Aposentadoria']=aposent
print('---'*15)
print('=-='*15)
for k,v in cadastro.items():
    print(f'{"-":<2}{k} tem o valor {v}')
print('=-='*15)
'''
#exercicio93
'''
print('***'*15)
tot=0
gol=[]
nome=str(input('Nome do jogador: '))
cadastro={'Nome':nome}
partidas=int(input(f'Quantas partidas o {nome} jogou? '))
for c in range(0,partidas): 
    gol.append(int(input(f'Quantos gols foram feitos na partida {c+1}: ')))
cadastro['Gols']= gol[:] #sempre assim que se adiciona LISTA em dicionario
cadastro['Total']=sum(gol)
print('***'*15)
print('---'*20)
print(cadastro)
print('---'*20)
print('='*20)
for k,v in cadastro.items():
    print(f'No campo {k} tem o valor em {v}')
print('='*20)
print(f'O jogador {nome}, jogou {partidas} partidas.')
for i,v in enumerate(gol):
    print(f'Na partida {i+1}, ele fez {v} gols ')
print(f'O total é {sum(gol)}')

'''

'''
#exercicio94
#completo com listas e dicionarios
pessoas={}
galera=[]
som=med=0
print('=-='*30)
while True:
    pessoas.clear
    pessoas['Nome']=str(input('Nome: '))
    while True:
        pessoas['Sexo']=str(input('Sexo:[M/F] '))[0].upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro,digite apenas M ou F')
    pessoas['Idade']=int(input('Idade:'))
    som+=pessoas['Idade']
    galera.append(pessoas.copy())
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
    elif esc not in 'SN':
        esc = str(input('ERRO! Por favor digite somente dentro das opções desejadas?[S/N] ')).strip().upper()[0]
print(galera)
med=som/len(galera)
print('=-='*30)
print(f'Ao todo  temos {len(galera)} pessoas cadastradas')
print(f'A soma das idades é igual a {som} e a média é igual a {med:5.2f}')
print('Mulheres cadastradas')
for p in galera:
    if p['Sexo']=='F':
        print(p["Nome"],end='')
print()
print('Lista de pessoas que estão com idade em cima da media:',end=' ')
for p in galera:
    if p['Idade']>med:
        print(f'{p["Nome"]},')

'''
#exerciciobaterponto
'''
funcionarios={}
geral=[]
print('=-='*20)
while True:
    funcionarios.clear()
    funcionarios['Nome']=str(input('Nome: '))    
    while True:
        funcionarios['Sexo']=str(input('Sexo: ')).upper().strip()[0]
        if funcionarios['Sexo'] in 'MF':
            break
        print('Erro!!! Apenas M ou F')
    funcionarios['Id']=str(input('Id: '))
    funcionarios['Entrada']=float(input('Horário de chegada: '))
    funcionarios['Saida']=float(input('Horário de saída: '))
    geral.append(funcionarios.copy())
    esc=str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if esc=='N':
        break
print('-----TABELA DE FUNCIONARIOS-----')
print('-=-'*20)
for p in geral:
    print(f'{"-":2<}Nome do funcionário: {p["Nome"]} ,Sexo: {p["Sexo"]}, Id: {p["Id"]},Entrada da Empresa{p["Entrada"]} horas ,Saída da Empresa{p["Saida"]} horas',end='')
    print()
print('-=-'*20)
'''


#exercicio95
'''


print('***'*15)
tot=0
gol=[]
partidas=list
nome=str(input('Nome do jogador: '))
cadastro={'Nome':nome}
partidas=int(input(f'Quantas partidas o {nome} jogou? '))
for c in range(0,partidas): 
    gol.append(int(input(f'Quantos gols foram feitos na partida {c+1}: ')))
cadastro['Gols']= gol[:] #sempre assim que se adiciona LISTA em dicionario
cadastro['Total']=sum(gol)

for i,v in enumerate(gol):
    print(f'Na partida {i+1}, ele fez {v} gols ')
print(f'O total é {sum(gol)}')
'''

