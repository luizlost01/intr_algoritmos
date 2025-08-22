qnt = int(input('Qual a quntidade de cigarros que você fuma por dia: '))
anos = int(input('Quantos anos já fuma: '))
cigarros= qnt * 365 * anos
temp_perdido = 10 * cigarros
resultado= temp_perdido/(60*24)
print(f'{resultado}')