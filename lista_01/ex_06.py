#Entrada de dados
horaAula = float(input('Digite quando você ganha por hora por aula: '))
horasMes = float(input('Digite quantas horas trabalho por mês: '))
descontoINSS = float(input('Digite o Desconto do INSS: '))

salarioLiquido = (horasMes * horaAula) / descontoINSS

#Saida de dados
print(f'Seu salário liquido deve ser de {salarioLiquido}')



