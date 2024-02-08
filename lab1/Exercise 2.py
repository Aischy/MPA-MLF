# Exercise 2.1

import numpy as np
import time

# Create a numpy array with shape 5x5, containing numbers from 24 to 0 (because from 25 to 0 we need to have an array of size 26 and not 25)

arr = np.arange(24, -1, -1).reshape(5, 5)

# Function to set all numbers smaller than the threshold to 0, using loops
def threshold_array_with_loop(arr, threshold):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] < threshold:
                arr[i, j] = 0
    return arr

# Function to set all numbers smaller than the threshold to 0, without loops
def threshold_array_without_loop(arr, threshold):
    arr[arr < threshold] = 0
    return arr

# Test the functions
threshold = 1000
print("Original array:")
print(arr)
print("\nArray after applying threshold with loops:")
print(threshold_array_with_loop(arr, threshold))
print("\nArray after applying threshold without loops:")
print(threshold_array_without_loop(arr, threshold))



# Time comparison using loops
start_time = time.perf_counter()
threshold_array_with_loop(arr.copy(), threshold)
loop_execution_time = time.perf_counter() - start_time

# Time comparison without loops
start_time = time.perf_counter()
threshold_array_without_loop(arr.copy(), threshold)
no_loop_execution_time = time.perf_counter() - start_time

print("\nExecution time with loops:", loop_execution_time)
print("Execution time without loops:", no_loop_execution_time)

##

# Exercise 2.2

import matplotlib.pyplot as plt
import numpy as np

numbs = {
      "1": np.array([[0, 1, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]), # 1
      "2": np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]]), # 2
      "3": np.array([[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 3
      "4": np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]), # 4
      "5": np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 5
      "6": np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 6
      "7": np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]), # 7
      "8": np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]), # 8
      "9": np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]), # 9
      "0": np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]), # 0
}

def show_in_digi(input_integer: int):
    # Int to str
    digits = str(input_integer)

    # Initialise the array
    digi_display = np.zeros((5, 0), dtype=int)

    for digit in digits:
        digit_array = numbs[digit]
        # Space between 2 digits
        if digi_display.size != 0:
            digi_display = np.concatenate((digi_display, np.zeros((5, 2), dtype=int)), axis=1)
        digi_display = np.concatenate((digi_display, digit_array), axis=1)

    # Afficher l'affichage numérique
    plt.imshow(digi_display, cmap='binary_r')
    plt.show()

show_in_digi(1234567890)






















