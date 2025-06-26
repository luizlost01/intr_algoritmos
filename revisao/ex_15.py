v = 1
while v != 0:
    v = int(input("Digite um número inteiro (0 para sair): "))
    if v % 2 == 0 and v != 0:
        print(f"Você digitou um número par: {v}")
    elif v == 0:
        print("Você digitou zero, encerrando o programa.")
    else:
        print(f"Você digitou um número ímpar: {v}, não será impresso.")
#Decks Esteve aqui 
