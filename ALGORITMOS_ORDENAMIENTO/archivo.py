import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_time(arr, sort_function):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Tamaños de las listas a ordenar
sizes = [100, 500, 1000, 2000, 5000, 10000]

insertion_times = []
merge_times = []

for size in sizes:
    random_list = random.sample(range(1, size + 1), size)

    insertion_time = measure_time(random_list.copy(), insertion_sort)
    insertion_times.append(insertion_time)

    merge_time = measure_time(random_list.copy(), merge_sort)
    merge_times.append(merge_time)

# Crear gráfico lineal
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución entre Insertion Sort y Merge Sort')
plt.legend()
plt.grid(True)

# Guardar el gráfico como una imagen JPG
plt.savefig('tiempos_ejecucion.jpg')

# Mostrar el gráfico
plt.show()
