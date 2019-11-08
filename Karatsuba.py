import math


def karatsuba(u, v):
    x = str(max(u, v))
    y = str(min(u, v))
    n_half = math.ceil(len(x) / 2)
    a = int(x[:(n_half-1)])
    b = int(x[(n_half-1):])
    if len(y) <= n_half:
        c = 0
        d = int(y)
    else:
        c = int(y[:(len(y) - n_half)])
        d = int(y[(len(y) - n_half):])

    print(n_half)
    print(a, b, c, d)


karatsuba(4567, 334)
