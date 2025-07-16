from typing import List

def solve(nums:List[int], threshold:int)->int:
        print(f"nums: {nums}, threshold: {threshold}")
        count = 0
        for i in nums:
            if i >= threshold:
                count += 2
            else:
                count += 1

        return count

l, n = [2, 8, 25, 18, 99, 11, 17, 16], 17
result = solve(l, n)
print(result)
