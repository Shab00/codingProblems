GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def length_of_longest_substring(s):
    l = 0
    seen = set()
    count = 0

    for r in range(len(s)):
        
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        
        seen.add(s[r])
        count = max(count, r - l + 1)

    return count

tests = [
    ("abcabcbb", 3),
    ("bbbbb",    1),
    ("pwwkew",   3),
    ("",         0),
    ("a",        1),
    ("au",       2),
    ("dvdf",     3),
    ("abba",     2),
]

for i, (s, expected) in enumerate(tests, 1):
    result = length_of_longest_substring(s)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
