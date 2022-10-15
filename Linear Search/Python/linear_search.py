
def linearSearch(arr, data):
    for i in range(0, len(arr)):
        if (arr[i] == data):
            return i
    return -1


arr = [12, 21, 8, 16, 34, 51, 6]
data = 18

result = linearSearch(arr, data)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index", result)
