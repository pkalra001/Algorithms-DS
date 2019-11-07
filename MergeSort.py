A = [4, 7, 2, 2, 1, 3]


def mergee(a, b, B):
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            B[k] = a[i]
            k += 1
            i += 1
        else:
            B[k] = b[j]
            j += 1
            k += 1

    while i < len(a):
        B[k] = a[i]
        k += 1
        i += 1

    while j < len(b):
        B[k] = b[j]
        k += 1
        j += 1


def mergee_sort(arr):
    if len(arr) == 1:
        return
    a = arr[0:len(arr) // 2]
    mergee_sort(a)
    b = arr[len(arr) // 2:]
    mergee_sort(b)
    mergee(a, b, arr)


mergee_sort(A)
print(A)
