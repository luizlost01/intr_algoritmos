#Entrada de dados
cotacao = float(input('Insira o valor da cotação do dólar: '))
quantidade_dolares = float(input('Insira a quantidade de dólares: '))
valor_reais = cotacao * quantidade_dolares

#Saida de dados
print(f'O valor em reais é: {valor_reais:.2f} R$')