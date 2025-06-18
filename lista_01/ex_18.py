# Leitura dos votos válidos para cada candidato
votos_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
votos_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
votos_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))
# Leitura dos votos nulos e em branco
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_brancos = int(input("Digite a quantidade de votos em branco: "))
# Cálculo do total de eleitores
total_eleitores = votos_a + votos_b + votos_c + votos_nulos + votos_brancos
# Cálculo dos percentuais
percentual_a = (votos_a / total_eleitores) * 100
percentual_b = (votos_b / total_eleitores) * 100
percentual_c = (votos_c / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_brancos = (votos_brancos / total_eleitores) * 100
# Exibição dos resultados
print(f"\nTotal de eleitores: {total_eleitores}")
print(f"Percentual de votos válidos do candidato A: {percentual_a}")
print(f"Percentual de votos válidos do candidato B: {percentual_b}")
print(f"Percentual de votos válidos do candidato C: {percentual_c}")
print(f"Percentual de votos nulos: {percentual_nulos}")
print(f"Percentual de votos em branco: {percentual_brancos}")