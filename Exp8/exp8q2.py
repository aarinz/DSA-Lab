def binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        
        if k == arr[m]:
            return m
        elif k < arr[m]:
            r = m - 1 
        else:
            l = m + 1 
            
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 7]
    k = 4
    index = binary_search(arr, k)
    print(f"Index of {k} is: {index}")  # Output: Index of 4 is: 3
