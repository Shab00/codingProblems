MOD = 10**9 + 7


def solve(a: list[int]) -> int:

    a.sort()
    l = len(a)
    if l < 3:
        return abs(a[1] - a[0])
    firstHalf = a[:l//2]
    secondHalf = a[l//2:]

    firstAv = sum(firstHalf) / len(firstHalf)
    secondAv = sum(secondHalf) / len(secondHalf)

    num = abs(secondAv - firstAv)

    return num

inputs = [[1, 2, 10, 11], 
          [1, 2, 3], 
          [64,32,64,16,64,0], 
          [4,2,5,7,7,0,7]
          ]

for i in inputs:
    result = solve(i)
    print(result)
