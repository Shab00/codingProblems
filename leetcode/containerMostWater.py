def maxArea(height: list[int]) -> int:
    pass


# def brute(height: list[int]) -> int:

    # p = 0
    # result = []
    # maxResult = 0
    # while p <= len(height) - 1:
        
        # for position, pillar in enumerate(height[p:], start = 1):
            # curResult = min(height[p:][0], pillar) * (position - 1)
            # maxResult = max(maxResult, curResult)
        # p += 1

    # return maxResult


inputs = [([1,8,6,2,5,4,8,3,7], 49), ([1,1], 1)]

for l, e in inputs:
    results = maxArea(l)
    print(f"input: {l} || output: {results} || expected: {e}")
