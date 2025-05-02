def solve(n:int, k:int) -> int:
        print(f"n: {n}, k: {k}")
        
        while k > 0:
            if n % 10 == 0:
                n //= 10
                k -= 1
            else:

                n -= 1
                k -= 1
        return n

n, k = 512, 4

result = solve(n, k)

print(result)
