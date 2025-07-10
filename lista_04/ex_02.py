# Algoritmo para determinar os campeões de um campeonato de futebol

def main():
    pontuacoes = []
    
    # Solicita o número de times
    while True:
        try:
            n_times = int(input("Digite o número de times (máximo 50): "))
            if 1 <= n_times <= 50:
                break
            else:
                print("Número de times deve ser entre 1 e 50.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Lê as pontuações dos times
    print(f"\nDigite as pontuações dos {n_times} times:")
    for i in range(n_times):
        while True:
            try:
                pontuacao = int(input(f"Pontuação do time {i+1}: "))
                if pontuacao >= 0:
                    pontuacoes.append(pontuacao)
                    break
                else:
                    print("A pontuação deve ser um número não negativo.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    # Encontra a maior pontuação (campeões)
    maior_pontuacao = max(pontuacoes)
    
    # Conta quantos times tiveram a maior pontuação
    campeoes = pontuacoes.count(maior_pontuacao)
    
    # Mostra os resultados
    print(f"\n{'='*50}")
    print("RESULTADO DO CAMPEONATO")
    print(f"{'='*50}")
    print(f"Pontuação dos campeões: {maior_pontuacao} pontos")

    print(f"\nTimes campeões:")
    for i, pontuacao in enumerate(pontuacoes):
        if pontuacao == maior_pontuacao:
            print(f"- Time {i+1} com {pontuacao} pontos")

main()