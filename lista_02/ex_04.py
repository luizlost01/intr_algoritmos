'''
4. Leia um valor numérico inteiro. O algoritmo deve apresentar a mensagem “ O valor esta na
faixa permitida” , caso o valor informado esteja entre 1 e 9. Se o valor estiver fora da faixa, o
programa deve apresentar a mensagem “O valor esta fora da faixa permitida” .
'''

# Entrada de dados
valor = int(input('Digite um valor: '))

if valor >=1 and valor <= 9:
    print('O valor está na faixa permitida')
else:
    print('O valor está fora da faixa permitida')
    