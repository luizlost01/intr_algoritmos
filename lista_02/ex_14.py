#Entrada de Dados
salario = float(input('Digite o salário do funcionário: '))
if salario <= 400.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Salário atual: R${salario:.2f}, Aumento: R${aumento:.2f}, Novo salário: R${novo_salario:.2f}')
elif salario <= 700.00:
    aumento = salario * 0.12
    novo_salario = salario + aumento
    print(f'Salário atual: R${salario:.2f}, Aumento: R${aumento:.2f}, Novo salário: R${novo_salario:.2f}')
elif salario <= 1000.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Salário atual: R${salario:.2f}, Aumento: R${aumento:.2f}, Novo salário: R${novo_salario:.2f}')
elif salario <= 1800.00:
    aumento = salario * 0.07
    novo_salario = salario + aumento
    print(f'Salário atual: R${salario:.2f}, Aumento: R${aumento:.2f}, Novo salário: R${novo_salario:.2f}')
elif salario <= 2500.00:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    print(f'Salário atual: R${salario:.2f}, Aumento: R${aumento:.2f}, Novo salário: R${novo_salario:.2f}')
else:
    print(f'Salário atual: R${salario:.2f}, Aumento: R$0.00, Novo salário: R${salario:.2f}')