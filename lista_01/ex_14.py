# Entrada de dados
quantidade_balas = int(input("Digite a quantidade de balas a serem distribuídas: "))
numero_pessoas = int(input("Digite o número de pessoas: "))

balas_por_pessoa = quantidade_balas // numero_pessoas
balas_sobrando = quantidade_balas % numero_pessoas

# Saída de dados
print(f"Cada pessoa recebeu {balas_por_pessoa} balas.")
print(f"Sobrou {balas_sobrando} balas na divisão.")