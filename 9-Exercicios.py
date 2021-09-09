#exercicio66
'''n = soma = cont = 0
while True:
    n = int(input('Digite um número[999 para confirmar]: '))
    if n == 999:
        break 
    soma += n
    cont += 1
print(f'Foram  {cont} valores impresso, a somas deles é {soma} ')
print('Obrigado')'''

#exercicio67
'''
multi=0
while True:
    n=int(input('Digite o número que você saber a tabuada: '))
    if n<0:
        break
    print('-'*20)
    for c in range (1,11):
        multi=n*c
        print(f'{n}X{c}={multi}')
    print('-'*20)
print('Fim')'''

#exercio 68
'''
from random import randint
cont= 0
veri=0
resultado = 0
while True:
    print('=-='*20)
    print('Vamos jogar Impar ou Par')
    print('=-='*20)
    n = int(input('Escolha um número: '))
    es= str(input('Impar ou par:[I/P]')).strip().upper()[0]
    comp= randint(0,11)
    soma = n+comp
    resultado= soma % 2
    if es== 'P':
        if resultado == 0:
            print('Voce ganhou')
            print(f'Número escolhido pelo computador foi {comp} o seu foi {n} a soma foi igual a {soma}')
            cont+=1
        else:
            print('Deu Impar')
            print(f'Você Perdeu,número escolhido pelo computador foi {comp} o seu foi {n} a soma foi igual a {soma}')
            print(f'Número de vitorias foi:{cont}')
            break
    if es== 'I':
        if resultado != 0:
            print('Voce ganhou')
            print(f'Número escolhido pelo computador foi {comp} o seu foi {n} a soma foi igual a {soma}')
            cont+=1
        else:
            print('Deu Par')
            print(f'Você Perdeu,número escolhido pelo computador foi {comp} o seu foi {n} a soma foi igual a {soma}')
            print(f'Número de vitorias foi:{cont}')
            break
            
    '''

    #exericio69
'''idade=0
idademaior=0
homem=0
maioridademulher=0
cont=0
sexo = ''
while True:    
    print('-=-'*20)
    print('CADASTRE UMA PESSOA')
    print('-=-'*20)
    idade=int(input('Digite a idada desejada: '))
    sexo= str(input('Escolha o sexo: [M/F]')).strip().upper()[0]
    if idade>18:
        idademaior+=1
    if sexo in 'Mm':
        homem= homem +1
    if sexo in 'Ff' and idade<20:
        maioridademulher+=1
    veri=str(input('Deseja continusar?[S/N]: ')).strip().upper()[0]
    cont +=1
    print('---'*20)
    if veri in 'Nn':
        break
    
print(f'Total de pessoas cadastradas maior de 18 são: {idademaior}')
print(f'Ao total temos {homem} homens no cadastro.')
print(f'Ao todo existem {maioridademulher} mulheres menores de 20 anos no cadastro')'''
    
#exericio69 guanabara
'''tot18=totalh=mu20=0
while True:
    idade=int(input('Digite a idada desejada: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo= str(input('Escolha o sexo: [M/F]')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        totalh+=1
    if sexo == 'F' and idade<20:
        mu20+=1
    resp=' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print('Acabou')
print(f'Total de pessoas com mais de 18 anos é: {tot18}')
print(f'Total de homens é de {tot18}') 
print(f'Total de mulhres com menos de 20 anos é {mu20}')     '''

#exercicio70 SuperBaratão
''''
total=0
produto1000=0
menorpreco=0
cont=0
barato= ''
print('=-='*20)
print('Super Baratao')
print('=-='*20)
while True:
    nome=str(input('Digite o nome do produto: '))
    preco=float(input('Digite o preço dos produtos:'))
    cont+=1
    total+=preco
    escolha=' '
    escolha= str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if cont==1:
        menor = preco
        barato=nome
    else:
        if preco<menor:
            menor=preco
            barato = nome
    if preco >=1000:
        produto1000+=1
    while escolha not in 'SN':
        escolha= str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    print('---'*20)
print('*'*20)
print(f'O valor total das suas compras é {total:.2f}')
print(f'Produtos acima de 1000 são  {produto1000:.2f}')
print(f'O Produto com menor valor é [a/o]{barato}, custando o valor de :{menor:.2f}')
'''
'''#exercicio71
print('=-='*15)
print('{:^30}'.format('Banco Cev'))
print('=-='*15)
cont=0
valor=int(input('Qual valo você deseja sacar RS: '))
total=valor
céd = 50
totcéd=0
while True:
    if total>=céd:
        total -=céd
        totcéd+=1
    else:
        print(f'Total de {totcéd} cédulas de RS{céd}')
        if céd ==50:
            céd=20
        elif céd==20:
            céd=10
        elif céd==10:
            céd=1
        totcéd=0
        if total ==0:
            break
'''