#exercicio100
'''
from random import randint
from time import sleep

def sorteia(list):
    print('Sorteando os números desejados...',end=' ')
    for c in range(0,5):
        sleep(0.3)
        list.append(randint(0,50))
        print(list[c],end=' ')

def paressoma(list):
    soma=0
    for c in list:
        if c%2==0:
            soma+=c
    print(f'Soma é {soma}')


#principal
numeros=[]
sorteia(numeros)
paressoma(numeros)
'''

'''
from random import randint
from time import sleep

def sorteia(lst):
    print('Números sorteados: ')
    for c in range(0,5):
        sleep(0.4)
        lst.append(randint(0,80))
        print(lst[c],end=' ',flush=True)

def somaspares(lst):
    soma=0
    for c in lst:
        if c%2==0:
            soma+=c
    print(f'Soma é {soma}')


num=[]
sorteia(num)
somaspares(num)
'''

'''
from random import randint
from time import sleep

def sorteia(lst):
    print('Sorteando valores: ')
    for c in range(0,5):
        lst.append(randint(0,10))
        print(f'{lst[c]}',end='-')
def men(lst):
    soma=1
    for c in lst:
        if c % 2==0:
            soma*=c 
    print(f'A diminuicao é {soma}')


numeros=[]
sorteia(numeros)
men(numeros)
'''

'''
def fatorial(num =1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f


n=int(input('Digite o valor: '))
print(f'{fatorial(n)}')
'''


'''
#exericio101

def voto(ano):
    #quando o import é dentro da função, ele esta reduzido a funcionar somente aqui.
    import datetime
    atual= datetime.date.today().year
    idade=atual-nasc
    if idade < 16:
        return(f'Com {idade} anos. Nao Vota')
    elif 16 <= idade < 18 or idade>65 :
        return (f'Com {idade} anos. É Opcional')
    else:
        return (f'Com {idade} anos. É Obrigatório')

#programa principal
nasc=int(input('Digite o ano de nascimento: '))
print(voto(nasc))
'''
#exercicio102
'''
def fatorial(num,show=False):
    
    fatorial(n,showFalse)
    -> Calcula fatorial
    return f para retorna o valor do fatorial---------

    '''
'''
#exercicio103
    f=1
    for c in range (num,1,-1):
        f*=c
        if show==True:
            print(c,end=' ')
            if c>1:
                print('X',end=' ')
            else:
                print(' = ',end=' ')
    return f

#programaPrincipal
print(fatorial(5,show=True))
'''
'''
#exercicio103
def ficha(jog='Desconhecido',gol=0):
    print(f'O jogador {jog} fez  {gol} gols')
    

#programa Principal
        
n=str(input('Digite o nome do jogador: '))
g=str(input('Quantos gols: '))
if g.isnumeric():
    g= int(g)
else: 
    g=0

if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)
    '''
#exercicio105
'''
def leiaint(x):
    ok=False
    valor=0
    while True:         
        n=str(input(x))
        if n.isnumeric():
            valor= int(n)
            ok=True
        else:
            print('Erro')
        if ok:
            break
    return valor

#funcao principal
n= leiaint('Digite um número')
print(f'Você acabou de digitar o número {n}')
'''
'''
def leiaint(num):
    status=False
    valor=0
    while True:
        num=str(input('Digite um número: '))
        if num.isnumeric():
            valor= int(num)
            status=True
        else:
            print('Erro....Tente novamente')
        
        if status:
            return valor

#funcao Principal
n=leiaint('Digite um número')
print(f'O número digitado foi {n}')
'''
#exercicio105
#coisas importantes para dicionario
'''
def notas(*n,sit=False):
    r=dict()
    r['Notas']=n
    r['Total']=len(n)
    r['Maior']=max(n)#pra saber o maior é so digitar max
    r['Menor']=min(n)   #pra saber o menor é só colocar min
    r['Media']=sum(n)   #soma é só usar o sum
    if sit:
        if r['Media']>=7:
            r['Situação']='Boa'
        elif r['Media']<=5:
            r['Situação']='Razoavel'
        elif r['Media']>3:
            r['Situação']='Ruim'
    return r


notas(1,3,4)
'''
c=('\033[m',#0 = sem cor
'\033[0;30;41m'#vermelho
)

def HelpPy(ajuda):
    help(ajuda) 

def titulo(msg,cor=0):
    print(c[cor],end='')
    tam=len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0],end='')


#programa principal
while True:
    titulo(f' {"Sistema de ajuda PyHelp":>3}')
    from time import sleep
    comando=str(input('Função ou Biblioteca: '))
    print(f'Acessando a biblioteca {comando}')
    sleep(0.3)
    if comando.upper=='FIM':
        break
    else:
        HelpPy(comando)
print('Até Logo',1)

'''
#a=str(input('Digite valor: '))
#print(help(a))
'''