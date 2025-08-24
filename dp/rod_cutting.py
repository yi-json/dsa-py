"""
Given a rod of length n inches and an array price[].
price[i] denotes the value of a piece of length i. 
The task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Input: prices =  [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation:  The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.
"""

def top_down_helper(p, n):
    r = [float('-inf')] * (n + 1)
    return top_down(p, n, r)

def top_down(p, n, r):
    # o(n^2)
    if r[n] >= 0:
        return r[n]
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i-1] + top_down(p, n - i, r))
    r[n] = q
    return q

def bottom_up(p, n):
    # o(n^2)
    r = [float('-inf')] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    return r[n]

p = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(p)

print(top_down_helper(p, n))
print(bottom_up(p, n))