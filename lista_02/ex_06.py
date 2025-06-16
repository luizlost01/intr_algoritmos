'''
6. Escreva um algoritmo que lê um inteiro e determina e mostra se ele e impar
ou par
'''

# Entrada de dados
numero = int(input("Digite um número inteiro: "))
# Verificação de paridade
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")