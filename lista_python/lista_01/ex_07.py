#Entrada de Dados
tempo_viagem = float(input("Informe o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Informe a velocidade média (em km/h): "))

km_litro = 12
distancia = tempo_viagem * velocidade_media
litros_usados = distancia / km_litro

#Saida de dados
print(
    f"Sua velocidade média foi de {velocidade_media} km/h\n"
    f"O tempo gasto em sua viagem foi de {tempo_viagem} horas\n"
    f"Sua distância percorrida foi {distancia} km\n"
    f"Quantidade de litros utilizada na viagem: {litros_usados:.2f} litros"
)

