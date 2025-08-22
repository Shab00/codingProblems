def topKf(nums: list[int], k: int) -> list[int]:

    hMap = {}
    result = []
    for n in nums:
        if n not in hMap:
            hMap[n] = 0

        hMap[n] += 1
    
    for i in range(k):
        if not hMap:
            break
        mv = max(hMap.values())
        to_remove = []
        for key, value in hMap.items():
            if value == mv:
                result.append(key)
                to_remove.append(key)
        for key in to_remove:
            hMap.pop(key)
    return result[:k]

inputs = [([1,1,1,2,2,3], 2, [1,2]),
          ([1], 1, [1]),
          ([1,2], 2, [1,2])]

for i, k, e in inputs:
    result = topKf(i, k)
    print(
        f"inputs:\n{i}\n"
        f"outputs:\n{result}\n"
        f"expected:\n{e}\n"
        f"{'-'*40}\n"
        )
