MOD = 10**9 + 7


def solve(a: list[int]) -> int:

    a.sort()
    l = len(a)
    if l < 3:
        return abs(a[1] - a[0])
    firstHalf = a[:l//2]
    secondHalf = a[l//2:]
    if l % 2 == 0:
        firstAv = sum(firstHalf) // len(firstHalf)
        secondAv = sum(secondHalf) // len(secondHalf)
        num = abs(secondAv - firstAv)
        return num
    else:
        numer = abs(sum(secondHalf) * len(firstHalf) - sum(firstHalf) * len(secondHalf))
        dem = len(firstHalf) * len(secondHalf)
        return (numer * pow(dem, MOD-2, MOD)) % MOD

#result = ( numerator × modinv(denominator, MOD) ) 

#    Numerator: (\text{sum2} \times \text{count1} - \text{sum1} \times \text{count2})
 #   Denominator: (\text{count1} \times \text{count2})

#Step 2: Always use absolute value (if required)

#If the problem wants the absolute difference:
#numerator = | sum2 × count1 − sum1 × count2 | 

inputs = [[1, 2, 10, 11], 
          [1, 2, 3], 
          [64,32,64,16,64,0], 
          [4,2,5,7,7,0,7]
          ]

for i in inputs:
    result = solve(i)
    print(result)
