# Write a program to implement binary search
def binary_search(arr, p):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < p:
            low = mid + 1
 
        elif arr[mid] > p:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 
# Test array
arr = [ 12, 33, 41, 50, 60 ]
x = 50
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")