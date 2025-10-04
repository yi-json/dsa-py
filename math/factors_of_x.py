def factors(n):
    """
    given a number n, return a list of all the integer factors of n
    """
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

n = 12
print(factors(n))
