#exercicio36
#casa = float(input('Digite o valor da casa R$: '))
#sal = float (input('Digite o seu salario R$: '))
#anos = int (input('Digite quantas anos você deseja pagar: '))
#meses= 12*anos
#valor = (casa/meses)
#if valor <= (sal/100)*30:
    #print('''Emprestimo foi liberado com sucesso
    #O valor da parcela é de {:.2f} em {} anos, formando o valor total de {:.2f}'''.format(valor,anos,casa))
#elif  valor >= (sal/100)*30:
    #print('O emprestimo foi negado!!!!')

    #exercicio37
#num = int(input('Digite o número desejado:' ))
#print('[ 1 ] Converter para binário')
#print('[ 2 ] Converter para octal')
#print('[ 3 ] Converter para hexadecimal')
#menu = int(input('Digite a sua escolha: '))
#if menu==1:
   # #print('O número {} foi convertido para {}'.format(num,bin(num)))
#elif menu==2:
 #   print('O número {} foi convertido para {}'.format(num,oct(num)))
#elif menu ==3:
 #     #print('O número {} foi convertido para {}'.format(num,hex(num)))

 #exercicio38

#n = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor:'))
#if n>n2:
 #   print('O maior número é {}'.format(n))
#elif n2>n:
 #   print('O maior número é {}'.format(n2))
#elif n==n2:
  #  print('Eles são iguais !!')
  
  #exericio39

#ano = int(input('Digite o ano do seu nascimento: '))
#conf = 2017 - ano
#c1= 18-conf
#if conf==18:
   # print('Vocẽ deve se alistar imediatamente')
#elif conf<=18:
   # print('''Quem nasceu em {} tem {} anos em 2017
    #ainda falta {} ano para o alistamento
    #previsto para {}'''.format(ano,conf,c1,2017+c1))
#elif conf>18:
 #   print('''Você está extremamente atrasado!!!!
  #  Quem nasceu em {} tem {} anos em 2017
   # voce deveria ter se alistado em a  {} anos atras
    #previsto para {}'''.format(ano,conf,-c1,2017-(-c1)))
   
#from datetime import date
#atual = date.today().year
#nasc = int(input('Ano de nascimento: '))
#idade = atual - nasc
#print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
#if idade == 18:
#    print('Voce deve se alistar imediatamente'.format)
#elif idade <18:
#    saldo = 18-idade
#    ano = atual + saldo
#    print('Ainda falta {} para alistamento, voce deveria te se alistado em {}'.format(saldo,ano))
#elif idade >18:    
 #    saldo = idade -18
  #   ano = atual-saldo
   #  print('VOce deveria ter alistado ha {} anos no ano de {}'.format(saldo,ano))

   #exercicio40 Média

#n1 = float(input('Digite a sua primeira nota: '))
#n2 = float(input('Digite a sua segunda nota: '))
#med = (n1+n2)/2
#print('Sua média foi {:.1f}'.format(med))
#if med <5:
#    print('Você está reprovado, por favor entre em contato com a coordenação.')
#elif med == 5 or med < 7:
#    print('Você está de recuperação,sua média ,por favor entre em contato com a coordenação.')
#elif med >= 7:
#    print('Você está aprovado.Boas ferias e boas festas :')

#exericio 41 atletlas
#import datetime
#ano = int(input('Digite o ano de nascimento: '))
#atual = datetime.date.today().year
#idade = atual-ano
#if idade <= 9:
#    print('O participante que nasceu em {}, e está com {} anos, deve participar da categoria Mirim'.format(ano,idade))
#elif idade <= 14:
#    print('O participante que nasceu em {}, e está com {} anos, deve participar da categoria Infantil'.format(ano,idade))
#elif idade <= 19:
#    print('O participante que nasceu em {}, e está com {} anos, deve participar da categoria Junior'.format(ano,idade))
#elif idade <= 25:
#    print('O participante que nasceu em {}, e está com {} anos, deve participar da categoria Senior'.format(ano,idade))
#elif idade >25:
#    print('O participante que nasceu em {}, e está com {} anos, deve participar da categoria Master'.format(ano,idade))
# #exercio42 imc
#peso = float (input('Digite o seu peso: '))
#altura = float (input('Digite sua altura: '))
#imc = peso / (altura*altura)
#print('Seu peso é {},sua altura é {} o seu IMC tem o resultado de {:.2f}'.format(peso,altura,imc))
#if imc <18.5:
 #   print('Você está abaixo do peso, por favor vá ao médico o mais breve possível!')
#elif imc <= 25:
#    print('Você está com o peso ideal, continue praticando exercicios e se alimentando bem para ficar longe de doenças e aumento de peso.')
#elif imc <=30:
 #   print('Você está acima do peso, por favor vá ao médico o mais breve possível!')
#elif imc <= 40:
#    print('Você está com obesidade, por favor vá ao médico o mais breve possível!')
#elif imc >40:
 #   print('Você está com obesidade morbida, por favor vá ao médico o mais breve possível!')
 
 #exercicio 43 analisador triangulo
#n1 = float(input('Digite o primeiro segmento: '))
#n2 = float(input('Digite o segundo segmento: '))
#n3 = float(input('Digite o terceiro segmento: '))
#if n1 == n2 == n3:
 #   print('Estes segmentos formam um triangulo',end='')
  #  if n1 != n2 != n3:
   #     print('Este é um triangulo Equilatero, ou seja , um triangulo com todos os segmentos iguais.')
    #if n1 != n2 != n3 != n1 :
     #   print('Este é um triangulo Escaleno, ou seja , um triangulo com todos os segmentos diferentes.')
   # else:
    #    print('Estes é um triangulo isoceles!')
#else:
 #   print('Estes segmentos não formam um triangulo!')]

 #exercicio44
#print('=================================Loja Sakzin=================================')
#n = int(input('Digite o valor do produto que você deseja: '))
##print('[1]- Avista-Dinheiro ou Cheque')
##print('[3]- Parcelado em 2x-Cartão')
#print('[4]- Parcelado em 3x-Cartão')
#m = int (input('Escolha a forma de pagamento: '))
#if m==1:
#    n1=(n*10)/100
 #   print('Sua comnpra de {} vai custar no final do processo de compra {}'.format(n,n-n1))
#elif m==2:
 #   n1=(n*5)/100
  #  print('Sua comnpra de {} vai custar no final do processo de compra {}'.format(n,n-n1))
#elif m==3:
#    print('Sua comnpra de {} vai custar no final do processo de compra {}'.format(n,n))
#elif m==4:
#    n1=(n*20)/100
#    print('Sua comnpra de {} vai custar no final do processo de compra {}'.format(n,n+n1))

