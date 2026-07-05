from collections import defaultdict

def get_minimum_window(original: str, check: str) -> str:
    cMap = defaultdict(int)
    formed = 0
    l = 0
    best = ""
    
    for char in check:
        cMap[char] += 1
    
    needed = len(cMap)
    
    for r in range(len(original)):
        if original[r] in cMap:
            cMap[original[r]] -= 1
            if cMap[original[r]] == 0:
                formed += 1
        
        while formed == needed:
            current_window = original[l:r+1]
            if best == "" or len(current_window) < len(best) or (len(current_window) == len(best) and current_window < best):
                best = current_window
            
            if original[l] in cMap:
                if cMap[original[l]] == 0:
                    formed -= 1
                cMap[original[l]] += 1
            l += 1
    
    return best

inputs = [
    ("cdbaebaecd", "abc", "baec"),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "b", ""), 
    ("aa", "aa", "aa"),
    ("abc", "abc", "abc"),
    ("ab", "abc", ""),
    ("bba", "ab", "ba"),
    ("abcde", "ace", "abcde"),
    ("aabbcc", "abc", "abbc"),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (original, check, expected) in enumerate(inputs, start=1):
    result = get_minimum_window(original, check)
    
    if result == expected:
        print(f"example: {idx} => '{result}' == '{expected}' => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => '{result}' != '{expected}' => {RED}FAIL{RESET}")
