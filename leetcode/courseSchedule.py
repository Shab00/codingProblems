class Node:
    def __init__ (course = None, pre = None):
        self.course = course
        self.pre = pre 

inputs = [(2, [[1,0]], True), (2, [[1,0],[0,1]], False)]

def cycle(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass


GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (course, pre, expec) in enumerate(inputs, start=1):
    result = cycle(course, pre)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
