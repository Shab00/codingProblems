from typing import List
def solve(nums: List[int]) -> List[bool]:

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    result = []
    for i in nums:
        if i < 1:
            result.append(False)
            continue
        root = int(i ** 0.5)
        if root * root != i:
            result.append(False)
            continue
        if is_prime(root):
            result.append(True)
        else:
            result.append(False)
    return result

inputs = [4, 5, 6]
result = solve(inputs)
print(result)
