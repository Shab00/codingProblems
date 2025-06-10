from collections import deque

def solve(n:int) -> int:
    onesZeros = []
    for num in range(1, n + 1):
        numString = str(num)

        if set(numString).issubset({'0', '1'}):
            onesZeros.append(num)

    return len(onesZeros)

def bfs(n:int) -> int:


    queue = deque("1")
    result = []
    while queue:
        curNum = queue.popleft()
        if int(curNum) <= n:
            result.append(curNum)
            queue.append(curNum + "0")
            queue.append(curNum + "1")

    return len(result)

def dfs(n: int) -> int:
    def helper(cur: str) -> int:
        if int(cur) > n:
            return 0
        count = 1  # cur is valid
        count += helper(cur + "0")
        count += helper(cur + "1")
        return count

    return helper("1")           

numbers = [10, 50, 100, 150, 500, 600, 700, 800, 900, 1000, 2000]
print(numbers)
for i in numbers:
    result = bfs(i)
    print(result)
