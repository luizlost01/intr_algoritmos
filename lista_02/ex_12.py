#Entrada de dados
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

result = num1 / num2

if result % 0:
    print(f'A Divisão de {num1} por {num2} é exata')
else:
    print(f'A Divisão de {num1} por {num2} não é exata')
