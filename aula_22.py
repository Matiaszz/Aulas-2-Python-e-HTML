lista_1 = []
for x in range(3):
    for y in range(3):
        lista_1.append((x, y))

lista_2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista_3 = [
    [(x, letra) for letra in "Nome"]
    for x in range(3)
]

print(lista_1)
print(lista_2)
print(lista_3)