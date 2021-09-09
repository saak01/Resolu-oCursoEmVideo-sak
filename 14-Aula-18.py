# Esse tipo de listas multiplas são chamadas de ligação
#pois quando é alterado um dos valores todos serão alterados.
'''
teste=list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste)
teste[0] ='Maria'
teste[1] = 22
galera.append(teste)
print(galera)
'''
#Desta forma podemos copiar e fazer alterações.
'''teste=list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0] ='Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

#outra forma de declarar listas compostas são:
'''galera=[['Joao',20],['Gustavo',44],['Bruno',13],['Bruninho',13]]
print(galera[0][0])'''
#lista com repetições
'''galera=[['Joao',20],['Gustavo',44],['Bruno',13],['Bruninho',13]]
for p in galera:
    print(p[1])
'''
#lista multiplas com input
galera=[]
dados=[]
for p in range(0,5):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()
print(f'{p[0]} e suas idades são {p[1]}')