# Entrada de dados
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
# Diferença
if valor1 > valor2:
    diferenca = valor1 - valor2
    print(f"A diferença é: {diferenca}")
else:
    diferenca = valor2 - valor1
    print(f"A diferença é: {diferenca}")
