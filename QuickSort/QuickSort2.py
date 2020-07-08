def QckSrt(arr, l, r, n_comp):
    if l == r or r < 0 or l > r:
        return n_comp
    n_comp += r - l
    p = arr[r]










































    i = l + 1
    j = l + 1
    while j <= r:
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    n_comp = QckSrt(arr, l, i - 2, n_comp)
    n_comp = QckSrt(arr, i, r, n_comp)
    return n_comp


file = open("QuickSort1.txt", "r")
a = []
for lines in file:
    a.append(int(lines))
# print(a)
# a = [2, 1, 12, 13, 16, 10, 9, 5, 18, 8, 17, 20, 19, 3, 4, 11, 14, 6, 7, 15]
print(QckSrt(a, 0, len(a) - 1, 0))
# print(a)
