GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def sort_colors(nums):
    
    low, mid, high = 0, 0,  len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

tests = [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 0, 1],           [0, 1, 2]),
    ([0],                 [0]),
    ([1],                 [1]),
    ([2],                 [2]),
    ([0, 0, 0],           [0, 0, 0]),
    ([1, 1, 1],           [1, 1, 1]),
    ([2, 2, 2],           [2, 2, 2]),
    ([0, 1, 2],           [0, 1, 2]),
    ([2, 1, 0],           [0, 1, 2]),
    ([1, 2, 0, 1, 2, 0],  [0, 0, 1, 1, 2, 2]),
    ([0, 0, 1, 1, 2, 2],  [0, 0, 1, 1, 2, 2]),
]

for i, (nums, expected) in enumerate(tests, 1):
    result = nums[:]
    sort_colors(result)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
