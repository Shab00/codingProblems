from collections import defaultdict

inputs = [(2, [[1,0]], [0,1]),
          (4, [[1,0],[2,0],[3,1],[3,2]], [0,2,1,3]),
          (1, [], [0]),
          (2, [[0,1],[1,0]], [])]

def findOrder(numCourses: int, pre: list[list[int]]) -> list:
    prereq_map = defaultdict(list)
    for course, prereq in pre:
        prereq_map[course].append(prereq)
    visiting = set()
    visited = set()
    result = []

    def dfs(course):
        if course in visiting:
            return False
        if course in visited:
            return True
        visiting.add(course)
        for prereq in prereq_map[course]:
            if not dfs(prereq):
                return False
        visiting.remove(course)
        visited.add(course)
        result.append(course)
        return True

    for c in range(numCourses):
        if not dfs(c):
            return []
    return result

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def is_valid_order(order, numCourses, pre):
    if order is None:
        return False
    if len(order) != numCourses:
        return False
    pos = {course: idx for idx, course in enumerate(order)}
    if set(order) != set(range(numCourses)):
        return False
    for ai, bi in pre:
        if pos[ai] < pos[bi]:
            return False
    return True

for idx, (course, pre, expected) in enumerate(inputs, start=1):
    result = findOrder(course, pre)
    valid = is_valid_order(result, course, pre) if result else (expected == [])
    if valid:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
