import time


def karat(u, v):
    if len(str(u)) < 3 or len(str(v)) < 3:
        return u * v
    n = max(len(str(u)), len(str(v))) // 2
    a = u // 10 ** n
    b = u % 10 ** n
    c = v // 10 ** n
    d = v % 10 ** n
    z0 = karat(a, c)
    z1 = karat((a + b), (c + d))
    z2 = karat(b, d)
    return z0*(10**(2*n)) + (z1-z0-z2)*(10**n) + z2


g = 3141592653589793238462643383279502884197169399375105820974944592
m = 2718281828459045235360287471352662497757247093699959574966967627
t1 = time.time()
print(g*m)
print(time.time()-t1)
t2 = time.time()
print(karat(g, m))
print(time.time()-t2)
