def sequential_search(arr, k):
    i = 0
    n = len(arr)
    
    while i < n and arr[i] != k:
        i += 1
    
    if i < n:
        return i
    else:
        return -1

# Example usage

arr = [4, 2, 7, 1, 3]
k = 7
index = sequential_search(arr, k)
print(f"Index of {k} is: {index}")  # Output: Index of 7 is: 2
