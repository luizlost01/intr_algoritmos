#Entrada de dados
cotacao = float(input('Insira o valor da cotação do dólar: '))
quantidade_reais = float(input('Insira a quantidade de reais: '))
valor_dolares = quantidade_reais / cotacao

#Saida de dados
print(f'O valor em dólares é: {valor_dolares:.2f} US$')