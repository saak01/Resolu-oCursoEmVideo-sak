'''
#exercicio82
listanum=[]
pares=[]
impar=[]
print('=-='*15)
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
print('-'*50)
print(f'Os números digitados foram: {listanum}')
print(f'Os números pares dessa lista são: {pares}')
print(f'Os números impares são: {impar}')
print('=-='*15)
'''
#exercicio83

'''
expre=str(input('Digite a expressão desejada: '))
pilha=[]
cont=cont1=0
for simb in expre:
    if simb == '(':
        cont+=1
    elif simb == ')':
        cont1+=1
if cont1 != cont:
    print('A equacao ta errada')
elif cont1 == cont:
    print('Expressão correta')
'''     
'''
#exercicio84v2
expre=str(input('Digite a expressão desejada: '))
pilha=[]
cont=cont1=0
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(expre)>0:
            pilha.append('(')
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Válido')
else:
    print('Invalido')
   ''' 

