depósito = float(input("Depósito inicial: ")) #pede para o usuário o deposito inicial.
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): ")) #pede para o usuário a taxa de juros
mês = 1 #Define "mês" com valor 1 
saldo = depósito 
while mês <= 24: #enquanto mês fos menor ou igual a 24
    saldo = saldo + (saldo * (taxa / 100)) #calcula o saldo
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.") #imprime o saldo de cada mês
    mês = mês + 1 #adiciona 1 no contador mês
    print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.") #imprime o ganho obtido no mês
#Este código mostra quanto o dinheiro depositado por uma pessoa rende á determinada taxa de juros, mostrando ao final quanto rendeu no total mês por mês, até comletar 24 meses.
