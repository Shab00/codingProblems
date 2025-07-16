def solve(ls1: list, ls2: list) -> list:
    result = set()
    ls2_set = set(ls2)
    for i in ls1:
        if i in ls2_set:
            result.add(i)
    return list(result)

test_cases = [
    ([[1,2,2,1], [2,2]], [2]),
    ([[4,9,5], [9,4,9,8,4]], [9,4])
]

for inputs, expected in test_cases:
    result = solve(*inputs)
    print(f"Input: {inputs} | Output: {result} | Expected: {expected}")
