'''
5. Leia o nome e o sexo de uma pessoa e apresente como saída uma das seguintes mensagens: “
Ilmo. Sr.”, caso seja informado o sexo como masculino, ou “ Ilma. Sra.”, caso seja informado o
sexo como feminino. O algoritmo deve apresentar junto com cada mensagem de saudação o
nome previamente informado.
'''

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