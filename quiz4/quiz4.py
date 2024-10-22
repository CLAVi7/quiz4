import random
import time

def listaAleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randint(0, n)
      return lista

def inicializar(sort, tamaño):
    iteraciones = 10
    time3 = 0.0
    for i in range (iteraciones):
        aleatorios = listaAleatorios(tamaño)

        start_time = time.time()
        if sort == "bubble_sort":
            bubble_sort(aleatorios)
        else:
            quicksort(aleatorios)
        fin_time = time.time()
        time3 += fin_time-start_time
    return time3/10

#https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(lista):
    # Outer loop to iterate through the list n times
    for n in range(len(lista) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if lista[i] > lista[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]


#https://www.geeksforgeeks.org/python-program-for-quicksort/
# Approach 2: Quicksort using list comprehension

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)

# Example usage



"""print(inicializar("bubble_sort", 1000))#retorna el promedio del tiempo
print(inicializar("bubble_sort", 2000))
print(inicializar("bubble_sort", 3000))
print(inicializar("bubble_sort", 4000))
print(inicializar("bubble_sort", 5000))"""

print(inicializar("quicksort", 1000))#retorna el promedio del tiempo
print(inicializar("quicksort", 2000))
print(inicializar("quicksort", 3000))
print(inicializar("quicksort", 4000))
print(inicializar("quicksort", 5000))