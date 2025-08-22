# Entrada de dados
salario_mensal = float(input("Insira o valor do salário mensal: "))
percentual_reajuste = float(input("Insira o percentual de reajuste: "))

novo_salario = salario_mensal + (salario_mensal * percentual_reajuste / 100)

# Saída de dados
print(f"O novo salário é: R$ {novo_salario:.2f}")