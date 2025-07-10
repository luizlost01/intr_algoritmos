lista = []

def media(lista):
    return sum(lista) / len(lista)

while len(lista) <= 9:
    n = int(input('Digite um numero: '))
    lista.append(n)

media_calculada = media(lista)
print(f'Media: {media_calculada}')

print(f'\nNúmeros maiores que a média ({media_calculada}):')
numeros_maiores = []
for numero in lista:
    if numero > media_calculada:
        numeros_maiores.append(numero)
        print(f'- {numero}')


