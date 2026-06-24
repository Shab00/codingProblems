inputs = [("Do geese see God?", True),
          ("Was it a car or a cat I saw?", True),
          ("A brown fox jumping over", False),
          ("A man, a plan, a canal: Panama", True)]

def find(s: str) -> bool:
    l, r = 0, len(n) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            
            l += 1
            r -= 1
    return True
        
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (n, expec) in enumerate(inputs, start=1):
    result = find(n)
    if result == expec:
        print(f"example: {idx} => {result} == {expec} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} != {expec} => {RED}FAIL{RESET}")

