# Entrada de dados
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

valores = [a, b, c]
valores.sort()

print(f'Os valores em ordem crescente são: {valores[0]}, {valores[1]}, {valores[2]}')