quantos = 0

for numero in range(1, 1001):
    if numero % 7 == 0 and numero % 2 == 0:
        quantos += 1

print(quantos)