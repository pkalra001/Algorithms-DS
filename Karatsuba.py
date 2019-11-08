import math


def karatsuba(u, v):
    x = str(max(u, v))
    y = str(min(u, v))
    n_half = math.floor(len(x) / 2)
    a = int(x[:n_half])
    b = int(x[n_half:])
    if len(y) <= (n_half + 1):
        c = 0
        d = int(y)
    else:
        c = int(y[:(len(y) - (n_half + 1))])
        d = int(y[(len(y) - (n_half + 1)):])

    print(n_half)
    print(a, b, c, d)


karatsuba(456786, 3365)
