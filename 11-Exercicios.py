#exercio72
'''
numero=0
esc=0
while esc<=20:
    esc=int(input('Digite um número entre 0 e 20 para saber por extenso: '))
    numero= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    for cont in range(0,len(numero)):
        if esc == cont:
            print(f'O número escolhido foi: {cont} ele por extenso é: {numero[cont]}')'''

#exercio73
'''
cont= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num=int(input('Digite um número entre 0 e 20 para saber por extenso: '))
    if 0 <= num <= 20:#entre
        break
    print('Tente novamente ',end=' ')
print(f'Voce digitou o numero: {cont[num]}')'''
#exercio74
'''print('=-='*20)
print('Tabela do Brasileirão')
print('=-='*20)
times='Bragantino','Athetico-Pr','Fortaleza','Bahia','Palmeiras','Atletico Goiano','Fluminense','Santos','Corithians','Ceara SC','Inter','Juventude','Sport','Cuiabá','São Paulo','Chapecoense','America MG','Gremio'
print('=-='*20)
print(f'Os cinco primeiros times da tabela são: {times[0:5]}')
print('=-='*20)
print(f'Os 4 ultimos colocados são{times[-4:]}')
print('=-='*20)
print(f'Os times em ordem alfabetica:{sorted(times)}')
print('=-='*20)
print(f'A colocação da chapecoense é {times.index("Chapecoense")+1}')'''

#exercio74 v2
''''
times='Bragantino','Athetico-Pr','Fortaleza','Bahia','Palmeiras','Atletico Goiano','Fluminense','Santos','Corithians','Ceara SC','Inter','Juventude','Sport','Cuiabá','São Paulo','Chapecoense','America MG','Gremio'
print('=-='*20)
print('TABELA DO BRASILEIRÃO')
for t in times:
   print(t)
print('__'*20)
times='Bragantino','Athetico-Pr','Fortaleza','Bahia','Palmeiras','Atletico Goiano','Fluminense','Santos','Corithians','Ceara SC','Inter','Juventude','Sport','Cuiabá','São Paulo','Chapecoense','America MG','Gremio'
print('__'*20)
print(f'Os cinco primeiros times da tabela são: {times[0:5]}')
print('__'*20)
print(f'Os 4 ultimos colocados são{times[-4:]}')
print('=-='*20)
print(f'Os times em ordem alfabetica:{sorted(times)}')
print('__'*20)
print(f'A colocação da chapecoense é {times.index("Chapecoense")+1}')'''

#exercio75 
'''
from random import randint
num= (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )
print('Os numeros sorteados foram.')
for n in num:
    print(f' {n}',end=' ')
print(f'\nO maior número foi {max(num)}')
print(f'O menores número foi {min(num)}')'''

#exercicio76
'''
num = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes')
print(f'O número 3 está na posição {num.index(3)+1}')
print('Os valores pares são:',end=' ')
for n in num:
    if n % 2 == 0:
        print(n,end=',') '''

#exercicio77
'''
palavras=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO',)
for p in palavras:
    print(f'\nA palavra {p} tem as vogais temos ',end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra,end=' ')

            '''
#76 v2
'''
print('--'*20)
print('Listagem de Preços')
print('--'*20)
listagem=('Lápis',1,75
,'Borracha',2,00,
'Caderno',15,90,
'Estojo',25,00,
'Transferidor',4.20
,'Compasso',9.90
,'Mochila',120.32
,'Caneta',22.30,
'Livro',34.90)
for pos in range(0,len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'{listagem[pos]:>10}')'''

#exercicio 77 v3
'''
print('=-='*15)
print(f'{"Preço Mercado":^40}')
print('=-='*15)
itens=('Farinha de Trigo',3.39,
'Oleo Vegetal',9.90,
'Massa de Bolo Aurora', 4.60,
'Ruflees',5.50,
'Caneta',2.00)
for pos in range(0,len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<40}',end="")
    else:
        print(f'RS{itens[pos]:>5}')
'''
print('=-='*15)
print(f'{"Lista de Preço V3":^40}')
print('=-='*15)
itens2=('Lampada',3.50,
'Cartão',60.60,
'Meia',15.50,
'Carregador',28.90,
'Mouse',190.90,
'Pincel',5.90)
for pos in range(0,len(itens2)):
    if pos % 2==0:
        print(f'{itens2[pos]:-<40}',end='')
    else:
        print(f'RS{itens2[pos]:>5}')
'''