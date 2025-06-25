v = 1
produto = 1
while v != 0:
    v = int(input("Digite um número inteiro (0 para sair): "))
    if v != 0:
        produto *= v
    else:
        print("Você digitou zero, encerrando o programa.")
print(f"O produto dos valores digitados é: {produto}")
