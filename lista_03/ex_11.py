#
sair = None

while True:
    nome_1 = (input('Nome de quem dara o lance: '))
    valor_1 = float(input(f'Valor do lance do(a) {nome_1}: '))
    
    nome_2 = str(input('Nome de quem dara o lance: '))
    valor_2 = float(input(f'Valor do lance do(a) {nome_2}: '))
    sair = input('Digite "sair" para encerrar ou pressione Enter para continuar: ').lower()
    if sair == 'sair':
        break

if valor_1 > valor_2:
    print(f'O(a) {nome_1} ganhou o leilao com o lance de R$ {valor_1}')
elif valor_2 > valor_1:
    print(f'O(a) {nome_2} ganhou o leilao com o lance de R$ {valor_2}')
else:
    print('Houve um empate entre os lances.')