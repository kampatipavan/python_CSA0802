def rotated_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = int(input("Enter target: "))

index = rotated_binary_search(arr, target)

if index != -1:
    print("Target found at index", index)
else:
    print("Target not found")