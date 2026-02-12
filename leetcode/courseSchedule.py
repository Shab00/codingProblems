inputs = [(2, [[1,0]], True), (2, [[1,0],[0,1]], False)]

def cycle(numCourses: int, prerequisites: list[list[int]]) -> bool:
    hMap = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        hMap[course].append(pre)
    visting = set()
    def dfs(course):
        if course in visting:
            return False
        if hMap[course] == []:
            return True  

        visting.add(course)

        for pre in hMap[course]:
            if not dfs(pre):
                return False

        visting.remove(course)

        hMap[course] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True



GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (course, pre, expec) in enumerate(inputs, start=1):
    result = cycle(course, pre)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
