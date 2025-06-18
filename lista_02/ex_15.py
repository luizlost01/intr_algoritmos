#Entrada de Dados

massa = float(input('Digite a massa (kg): '))
altura = float(input('Digite a altura (m): '))
imc = massa / (altura ** 2)

if imc < 20:
    faixa_risco = 'Abaixo do peso'
elif 20 <= imc < 25:
    faixa_risco = 'Normal'
elif 25 <= imc < 30:
    faixa_risco = 'Excesso de peso'
elif 30 <= imc < 35:
    faixa_risco = 'Obesidade'
elif imc >= 35:
    faixa_risco = 'Obesidade mórbida'

print(f'O IMC é: {imc:.2f}, Faixa de risco: {faixa_risco}')
