import random
import time

# ==============================================
# ORDENAMIENTO DE HEAP SORT
# ==============================================

def heapify(arr, n, i):
   
    mayor = i
    izquierdo = 2 * i + 1
    derecho = 2 * i + 2

    # Si el hijo izquierdo es mayor que la raíz
    if izquierdo < n and arr[izquierdo] > arr[mayor]:
        mayor = izquierdo

    # Si el hijo derecho es mayor que el mayor actual
    if derecho < n and arr[derecho] > arr[mayor]:
        mayor = derecho

    # Si el mayor no es la raíz
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]

        # Aplicar heapify nuevamente
        heapify(arr, n, mayor)

def heap_sort(arr, mostrar=False):
    n = len(arr)
    # --------------------------------------
    # 1. Construir Max Heap
    # --------------------------------------
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    if mostrar:
        print("\n2. Max Heap construido:")
        print(arr)
    # --------------------------------------
    # 2. Extraer elementos
    # --------------------------------------
    if mostrar:
        print("\n3. Estado del arreglo después de cada extracción:")
    for i in range(n - 1, 0, -1):
        # Intercambiar la raíz con el último elemento
        arr[0], arr[i] = arr[i], arr[0]
        if mostrar:
            print(f"Extracción: {arr}")
        # Restaurar el Max Heap
        heapify(arr, i, 0)
    # --------------------------------------
    # 3. Lista final
    # --------------------------------------
    if mostrar:
        print("\n4. Lista final ordenada:")
        print(arr)



if __name__ == "__main__":

    # ==========================================
    # EJERCICIO 7: DEMOSTRACIÓN DEL ALGORITMO HEAP SORT
    # ==========================================

    

    print("==========================================")
    print("        HEAP SORT - MAX HEAP")
    print("==========================================")

    print("\n1. Lista original:")
    datos = [12, 11, 13, 5, 6, 7]

    print(datos)
    lista = datos.copy()

    # Ejecutar Heap Sort mostrando los pasos
    heap_sort(lista, mostrar=True)

    # ==============================================
    # EJERCICIO 8: MEDICIÓN DE TIEMPOS DE EJECUCIÓN
    # ==============================================

    tamanos = [100, 500, 1000, 5000]

    print("\n========== MEDICIÓN DE TIEMPOS ==========")

    for cantidad in tamanos:

        # Generar lista aleatoria
        datos = [random.randint(1, 100) for _ in range(cantidad)]

        # Crear una copia para ordenar
        lista = datos.copy()

        # Iniciar cronómetro
        inicio = time.perf_counter()

        # Algoritmo Heap Sort
        heap_sort(lista)

        # Finalizar cronómetro
        fin = time.perf_counter()

        # Calcular tiempo
        tiempo = fin - inicio

        print(f"\nCantidad de elementos: {cantidad}")
        print(f"Tiempo de ejecución: {tiempo:.8f} segundos")


    # ==========================================
    # EJERCICIO 9
    # COMPORTAMIENTO DE LOS ALGORITMOS
    # ==========================================

    # Caso A: Lista aleatoria
    lista_aleatoria = random.sample(range(1, 10000), 1000)

    # Caso B: Lista ordenada
    lista_ordenada = list(range(1000))

    # Caso C: Lista ordenada inversamente
    lista_invertida = list(range(1000, 0, -1))


    # ----- Caso A -----

    lista = lista_aleatoria.copy()

    inicio = time.perf_counter()

    heap_sort(lista)

    fin = time.perf_counter()

    tiempo_aleatorio = fin - inicio


    # ----- Caso B -----

    lista = lista_ordenada.copy()

    inicio = time.perf_counter()

    heap_sort(lista)

    fin = time.perf_counter()

    tiempo_ordenada = fin - inicio


    # ----- Caso C -----

    lista = lista_invertida.copy()

    inicio = time.perf_counter()

    heap_sort(lista)

    fin = time.perf_counter()

    tiempo_invertida = fin - inicio

    print("\n==============================================")
    print("       EJERCICIO 9 - HEAP SORT")
    print("==============================================")

    print("\nResultados:")

    print("----------------------------------------------")
    print("Algoritmo    | Aleatoria | Ordenada | Invertida")
    print("----------------------------------------------")
    print(f"Heap Sort    | "f"{tiempo_aleatorio:.8f} | "f"{tiempo_ordenada:.8f} | "f"{tiempo_invertida:.8f}"
    )
    print("----------------------------------------------")    
