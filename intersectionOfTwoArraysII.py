def solve(n: list, r: list) -> list:
    dic = {}
    for i in r:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    result = []
    for i in n:
        if i in dic and dic[i] > 0:
            result.append(i)
            dic[i] -= 1
    return result

test_cases = [
    ([[1,2,2,1], [2,2,2]], [2, 2]),
    ([[4,9,5], [9,4,9,8,4]], [9,4])
]

for inputs, expected in test_cases:
    result = solve(*inputs)
    print(f"Input: {inputs} | Output: {result} | Expected: {expected}")
