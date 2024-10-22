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
            pass #quick_sort(aleatorios)
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

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
#https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)




print(inicializar("bubble_sort", 1000))#retorna el promedio del tiempo
print(inicializar("bubble_sort", 2000))
print(inicializar("bubble_sort", 3000))
print(inicializar("bubble_sort", 4000))
print(inicializar("bubble_sort", 5000))