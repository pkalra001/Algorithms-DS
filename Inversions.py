n_inversions = 0


def merge_sort(arr):
    if len(arr) == 1:
        return
    a = arr[:(len(arr)//2)]
    b = arr[(len(arr)//2):]
    merge_sort(a)
    merge_sort(b)
    merge(a, b, arr)


def merge(a, b, arr):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            n_inversion = len(a) - i
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


p = [1, 7, 6, 5, 4, 3, 2]
merge_sort(p)
print(p)



