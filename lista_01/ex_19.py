# Entrada de dados
altura = float(input("Insira a altura do cilindro (em metros): "))
raio = float(input("Insira o raio do cilindro (em metros): "))

area = 2 * 3.1415 * raio * (altura + raio)

litros_necessarios = area / 3
latas_necessarias = round(litros_necessarios / 5)
custo_total = latas_necessarias * 50

# Saída de dados
print(f"A área externa do cilindro é: {area:.2f} m²")
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Custo total para a pintura: R$ {custo_total:.2f}")
