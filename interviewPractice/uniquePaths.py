def uniquePaths_comb(m: int, n: int) -> int:
    # compute C(m+n-2, min(m-1,n-1)) using multiplicative formula
    N = m + n - 2
    k = min(m - 1, n - 1)
    if k == 0:
        return 1
    res = 1
    # compute product_{i=1..k} (N - k + i) / i using integer arithmetic
    for i in range(1, k + 1):
        res = res * (N - k + i) // i
    return res

# Examples
print(uniquePaths_comb(3, 7))  # 28
print(uniquePaths_comb(3, 2))  # 3
