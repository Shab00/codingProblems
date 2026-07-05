from collections import defaultdict

def get_minimum_window(original: str, check: str) -> str:

    cMap = defaultdict(int)
    formed = 0
    l = 0

    for char in check:
        cMap[char] += 1

    for r in original:
         
        

    return ""


inputs = [
    ("cdbaebaecd", "abc", "baec"),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "b", ""), 
    ("aa", "aa", "aa"),
    ("abaacbab", "abc", "bac"),
    ("abc", "abc", "abc"),
    ("ab", "abc", ""),
    ("bba", "ab", "ba"),
    ("abcde", "ace", "abcde"),
    ("aaabbbccc", "abc", "abc"),
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
