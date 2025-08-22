#Entrada de Dados

valorProduto = float(input('Digite o valor do produto: '))

if valorProduto <= 20:
    print(f'Valor para a venda: {valorProduto * 1.45}')
else:
    print(f'Valor para a venda: {valorProduto * 1.30}')    