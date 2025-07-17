valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite seu salário: R$ "))
anos_a_pagar = int(input("Digite em quantos anos quer pagar: "))

prestacao_mensal = valor_casa / (anos_a_pagar * 12)
if prestacao_mensal > (salario * 0.30):
    print('Emprestimo não permitido')
else:
    print('Emprestimo aprovado')