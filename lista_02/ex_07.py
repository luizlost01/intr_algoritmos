'''
7. Leia três valores para os lados de um triangulo (A, B e C). O algoritmo deve verificar se os
lados fornecidos formam realmente um triangulo, e se for esta condição verdadeira, deve ser
indicado qual tipo de triangulo foi formado: isósceles (dois lados iguais), escaleno (os três lados
diferentes) ou equilátero (três lados iguais). Para que três valores de lados formem um
triangulo, cada par de lados somados não pode ser menor ou igual ao terceiro lado.
'''

# Entrada de dados
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))
# Verificação se os lados formam um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    # Verificação do tipo de triângulo
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")