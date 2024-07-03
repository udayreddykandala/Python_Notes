from time import time


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Convert the input string to a list of integers
arr = list(map(int, input("Enter the array (comma-separated values): ").split(',')))
target = int(input("Enter the target value to search: "))

# Start the timer
start_time = time.time()

result = binary_search(arr, target)

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

if result == -1:
    print("Target not found")
else:
    print(f"Target found at index: {result}")

print(f"Time taken to execute the code: {elapsed_time:.10f} seconds")
