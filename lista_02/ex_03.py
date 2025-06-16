'''
3. Leia os valores de quatro notas escolares de um aluno. O algoritmo deve calcular a media
aritmética e apresentar a mensagem “ Aprovado” se a media obtida for maior ou igual a 7; caso
contrario, o algoritmo deve solicitar a nota de exame do aluno e calcular uma nova media
aritmética entre a nota do exame e a primeira media aritmética (NOVA_MEDIA =
MEDIA_ANTIGA * 0.6 + EXAME * 0.4). Se o valor da nova media for maior ou igual a 5,
apresentar a mensagem “ Aprovado em exame” ; caso contrario, apresentar a mensagem “
Reprovado”. O algoritmo deve também informar com cada mensagem o valor da media obtida.
'''

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
# Média
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"Aprovado! Média: {media}")
else:
    exame = float(input("Digite a nota do exame: "))
    nova_media = media * 0.6 + exame * 0.4
    if nova_media >= 5:
        print(f"Aprovado em exame! Nova média: {nova_media}")
    else:
        print(f"Reprovado! Nova média: {nova_media}")
