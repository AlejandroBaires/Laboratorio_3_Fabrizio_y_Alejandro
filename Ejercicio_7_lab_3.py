import random

datos = [random.randint(1, 100) for _ in range(20)]

print("Lista original:")
print(datos)

lista = datos.copy()