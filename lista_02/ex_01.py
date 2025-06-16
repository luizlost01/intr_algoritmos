'''
1 Leia os valores de quatro notas escolares de um aluno e calcule a sua media aritmetica,
apresentando o mensagem “ Aprovado” se a media obtida for maior ou igual a 5 ou a
mensagem “ Reprovado”, caso contrario. O algoritmo deve informar junto com cada mensagem
o valor da media obtida.
'''

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
# Média
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print(f"Aprovado! Média: {media}")
else:
    print(f"Reprovado! Média: {media}")
