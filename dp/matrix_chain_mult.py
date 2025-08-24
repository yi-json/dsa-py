"""
Given matrices A_1, A_2, ..., A_n, we want to find the product of
A_1 * A_2 * ... * A_n using as few scalar multiplications as possible
Note: Association property: (A_1 * A_2) * A_3 = A_1 * (A_2 * A_3)

Let m[i, j] = min # of scalar multiplications needed to compute A_{i,j}. End goal is m[1, n]
    * if i == j: m[i, i] = 0 for i = 1, ...,n
    * if i < j: m[i, j] = m[i, k] + m[k+1, j] + p[i-1] * p[k] * p[j] (must try every k) 
        * i.e left chain + right chain + cost to put them together

"""

def solve(p, n):
    dp = [[0] * n] * n 
    s = [[0] * n] * (n - 1)
    for l in range(1, n):
        for i in range(n-l+1):
            j = i + l + 1