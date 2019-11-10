def merge_sort_helper(arr, inv_count):
    if len(arr) == 1:
        return inv_count
    a = arr[:(len(arr)//2)]
    b = arr[(len(arr)//2):]
    inv_count = merge_sort_helper(a, inv_count)
    inv_count = merge_sort_helper(b, inv_count)
    return merge(a, b, arr, inv_count)


def merge(a, b, arr, inv_count):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            inv_count += len(a) - i
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
    return inv_count


def merge_sort(a):
    return merge_sort_helper(a, 0)


p = [4, 3, 2, 1]
print("No of inversions in the array are : "+ str(merge_sort(p)))
print(p)
