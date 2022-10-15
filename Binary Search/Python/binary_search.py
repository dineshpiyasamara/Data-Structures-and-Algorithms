
def binarySearch(arr, l, r, data):
    if r >= l:
        mid = (l + r) // 2
        if arr[mid] == data:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > data:
            return binarySearch(arr, l, mid-1, data)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, data)
    else:
        return -1


arr = [6, 8, 12, 16, 21, 34, 51]
data = 18
result = binarySearch(arr, 0, len(arr)-1, data)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index", result)
