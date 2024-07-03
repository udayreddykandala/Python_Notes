import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Convert the input string to a list of integers
arr = list(map(int, input("Enter the array (comma-separated values): ").split(',')))

# Start the timer
start_time = time.time()

# Perform the bubble sort
sorted_array = bubble_sort(arr)

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the sorted array and the time taken
print(f"Sorted array: {sorted_array}")
print(f"Time taken to execute the code: {elapsed_time:.10f} seconds")
