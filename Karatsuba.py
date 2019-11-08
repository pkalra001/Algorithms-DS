import math


def karatsuba(u, v):
    x = str(max(u, v))
    y = str(min(u, v))
    n_half = math.ceil(len(x)/2)
    a = x[:(n_half-1)]
    b = x[(n_half-1):]
    if len(y) <= n_half:










