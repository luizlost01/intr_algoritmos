'''
9. Escreva um algoritmo que, a partir de um numero inteiro de 0 a 10 informado pelo usuário
(testar se o número digitado está nessa faixa), escreva esse numero por extenso.
'''


# Entrada de dados
valor = int(input('Digite um valor: '))

if valor >=1 and valor <= 9:
    print('O valor está na faixa permitida')
else:
    print('O valor está fora da faixa permitida')
    