def solve(n:int, m:int)->int:

    count = 0
    while m > n: 
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        count += 1
    return count + (n - m) 

nAndM = [[10, 1], [2, 1], [99, 100], [666, 6666], [6666, 666]] 

for i in nAndM:
    n, m = i 
    result = solve(n, m)
    print(f"n = {n}, m = {m}, result = {result}")
