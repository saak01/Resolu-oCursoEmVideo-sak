#exercicio48
#for c in range(0,50,2):
 #   print(c, end=' ')
#exercicio49
#soma = 0
#cont = 0
#n1=int(input('Digite o valor para saber os multiplos de 3 e sua soma: '))
#n2=int(input('Digite o valor para saber os multiplos de 3 e sua soma: '))
#for c in range (n1,n2,2):
#    if c % 3 == 0:
#        cont= cont+1
#        soma = soma + c
#print('Os {} valores deram a soma de {}'.format(cont,soma))


#exercicio50
#n1 = int(input('Digite o número que você deseja receber a multiplicação: '))
#for c in range (1,11):
 #    print('{} X {} = {}'.format(n1,c,n1*c))

 #exercicio51
#n = int(input('Digite o número para a progressão aritmetica: '))
#r = int(input('Digite a razão:  '))
#dec = n + (10-1)*r
#for c in range (n,dec,r):
#    print(c,end=' → ')
#num= int(input('Digite o número que deseja para saber se é primo: '))
#tot = 0
#for c in range (1,num+1):
#    if num % c == 0:
#        tot += 1
#        print('\033[33m',end=' ')
#    else:
#         print('\033[31m',end=' ')
#         print('{}'.format(c),end=' ')
#print('\n\033[mO numero {} foi divisivel {} vezez'.format(num,tot))
#if tot == 2:
#    print('É primo')
#else:
#    print('nao primo')

#exercicio53

#frase = str(input('Escreva a texto para verificação do polimetro: ')).strip().upper
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range (len(junto)-1,-1):
#    inverso += junto [letra]
#    print(junto,inverso)
#if junto == inverso:
#    print('É palindromo')
#else:
#    print ('Não é palidromo')

#exercicio54
#from datetime import date, datetime
#atual = date.today().year
#totmaior=0
#totmenor=0
#for pess in range(1,8):
#    nasc= int(input('Em que ano a {}° a pessa nasceu? '.format(pess)))
#    idade = atual - nasc
#    if idade >=21:
#        totmaior+=1
#    else:       
#        totmenor+=1
#print('Ao total tivemos {} candidados mais velhos'.format(totmaior))
#print('Ao total tivemso {} candidatos novos'.format(totmenor))

#maior = 0
#menor = 0
#for p in range (1,6):
#    peso = float(input('Peso da {}° pessoa: '.format(p)))
#    if p == 1:
#        maior = peso
#        menor = peso
   # else:
   #     if peso > maior:
   #         maior= peso
   #     if peso< menor:
   #          menor = peso
#print('Maior peso lido foi {}'.format(maior))
#print ('Menor peso lido foi de {}'.format(menor))

#exericio55
#somaidade=0
#mediaidade = 0
#maioridadehomem= 0
#nomevelho=''
#cont=0
#for p in range(1,5):
   # print('{}° PESSOA'.format(p))
   # nome = str(input('Digite o seu nome: '))
   # idade = int(input('Digite a idade: '))
   # sexo = str(input('[M/F]')).strip()
   # somaidade += idade
   # if p == 1 and sexo in 'Mm':
   #     maioridadehomem = idade
    #    nomevelho = idade
    #if sexo in 'Mm' and idade > maioridadehomem:
   #     maioridadehomem = idade
  #      nomevelho = nome
 #   if sexo in 'Ff'and idade>20:
#        cont+=1

#mediaidade = somaidade / 4
#rint('A média de idade dos participantes foi de {}'.format(mediaidade))
#print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
#print('O número de mulheres menores de 20 anos é {}'.format(cont))