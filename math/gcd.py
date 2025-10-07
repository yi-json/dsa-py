
def gcd_iter(a, b):
    # euclidian_method
    while b:
        a, b = b, a % b
    return a

def gcd_recur(a, b):
    if b == 0:
        return a
    return gcd_recur(b, a%b)