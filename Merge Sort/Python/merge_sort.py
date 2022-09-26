def merge(array, lb, mid, ub):
    n1 = mid - lb + 1
    n2 = ub - mid

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[lb+i]

    for j in range(0, n2):
        R[j] = array[mid+1+j]

    i = 0
    j = 0
    k = lb
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def mergeSort(array, lb, ub):
    if lb < ub:
        mid = (lb+ub)//2
        mergeSort(array, lb, mid)
        mergeSort(array, mid+1, ub)
        merge(array, lb, mid, ub)
    return array


arr = [12, 6, 7, 8, 10, 2, 9, 11, 13, 12]

print("Before sorting : {}".format(arr))
mergeSort(arr, 0, len(arr)-1)
print("After sorting : {}".format(arr))
