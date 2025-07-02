def solve(nums: list[int]) -> list[int]:
    
    lenNum = len(nums)
    missing = []
    result = []

    for i in range(1, lenNum + 1):
        if i not in nums:
            missing.append(i)

    if not missing:
        return nums

    used = set(result)

    for j in nums:
        if j not in used and j not in missing:
            result.append(j)
            used.add(j)
        else:
            smallest = min(missing)
            result.append(smallest)
            used.add(smallest)
            missing.remove(smallest)


    return result

inputs = [[3, 2, 2, 3], 
          [5, 5, 5, 6, 4, 6], 
          [6, 8, 4, 6, 7, 1, 6, 3, 4, 5],
          [3, 1, 2],
          [2, 2, 1],
          [2, 2, 2]
          ]

for i in inputs:
    result = solve(i)
    print(result)
