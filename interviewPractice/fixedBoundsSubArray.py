inputs = [([1, 3, 5, 2, 3], 1, 5)]

def count_subarrays_fixed_bounds(nums, minVal, maxVal):
    last_min = last_max = -1
    last_invalid = -1
    res = 0
    for i, x in enumerate(nums):
        if x < minVal or x > maxVal:
            last_invalid = i
        if x == minVal:
            last_min = i
        if x == maxVal:
            last_max = i
        res += max(0, min(last_min, last_max) - last_invalid)
    return res

for i, j, k in inputs:
    result = count_subarrays_fixed_bounds(i, j, k)
    print(result)
