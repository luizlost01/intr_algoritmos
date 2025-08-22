# Entrada de dados
nome = input("Digite o nome: ")
sexo = input('Digite o sexo (M/F): ').upper()

if sexo == 'M':
    print(f'{nome}')
    print(f"Excelentissimo. Sr. {nome}")
    print('Seja Bem Vindo!')
else:
    print(f'{nome}')
    print(f"Excelentissima. Sra. {nome}")
    print('Seja Bem Vinda!')