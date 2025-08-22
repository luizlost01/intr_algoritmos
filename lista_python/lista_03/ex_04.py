quantidade_impares = 0
numero = int(input('Digite um número (0 para sair): '))
while numero != 0:
    if numero % 2 != 0:
        quantidade_impares += 1
    numero = int(input('Digite um número (0 para sair): '))
print(f'Quantidade de números ímpares digitados: {quantidade_impares}')
