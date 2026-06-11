def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid+1
        else:
            right=mid-1
    return -1 
     
arr = [3,7,9,14,22,27,35,41]
target = 27
idx = binary_search(arr,target)
print(f"Found at index{idx}")