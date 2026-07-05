def maximum_score(arr1: list[int], arr2: list[int]) -> int:
    l, r = 0, 0
    sum1, sum2 = 0, 0
    total = 0

    while l < len(arr1) and r < len(arr2):

        if arr1[l] < arr2[r]:
            sum1 += arr1[l]
            l += 1

        elif arr1[l] > arr2[r]:
            sum2 += arr2[r]
            r += 1
        else:
            total += max(sum1, sum2) + arr1[l]
            sum1 = 0
            sum2 = 0
            l += 1
            r += 1

    total += max(sum1 + sum(arr1[l:]), sum2 + sum(arr2[r:]))

    return total % (10**9 + 7)


inputs = [
    ([2, 4, 5, 8, 10], [4, 6, 8, 9], 30),
    ([1, 3, 5], [1, 3, 5], 9),
    ([1, 2, 3, 4], [2, 3], 10),
    ([1, 2, 3, 4, 5], [2, 4], 15),
    ([1, 2, 3], [1, 2, 3], 6),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 40),
    ([1, 5, 10, 15], [5, 10], 31),
    ([2, 3, 5, 6, 7, 9, 11, 13, 14, 16, 17, 19, 20], 
     [3, 4, 5, 7, 8, 10, 11, 12, 15, 16, 18, 20], 155),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (arr1, arr2, expected) in enumerate(inputs, start=1):
    result = maximum_score(arr1, arr2)
    
    if result == expected:
        print(f"example: {idx} => {result} == {expected} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expected} => {RED}FAIL{RESET}")
