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