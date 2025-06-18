n = int(input('Digite um número inteiro positivo: '))
soma = 0
soma_quadrados = 0
for i in range(1, n + 1):
    soma += i
    soma_quadrados += i ** 2
media = soma / n if n > 0 else 0
print(f'Somatório: {soma}')
print(f'Soma dos quadrados: {soma_quadrados}')
print(f'Média: {media:.2f}')
