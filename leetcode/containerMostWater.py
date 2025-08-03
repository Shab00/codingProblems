def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    maxResult = 0
    while l <= r:
        if height[l] <= height[r]:
            curResult = min(height[l], height[r]) * (r - l) 
            maxResult = max(maxResult, curResult)
            l += 1
        elif height[l] >= height[r]:
            curResult = min(height[l], height[r]) * (r - l) 
            maxResult = max(maxResult, curResult)
            r -= 1
    return maxResult

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
