def compress(s: str) -> str:
    if not s:
        return s

    l = 0
    count = 0
    parts = []
    
    for r in range(len(s)):
        if s[l] != s[r]:
            parts.append(s[l] + str(count))
            count = 0
            l = r
        count += 1
     
    parts.append(s[l]+ str(count))
    resString = "".join(parts)
    
    return resString if len(resString) < len(s) else s

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (s, expected)

    # 1. Book example
    ("aabcccccaaa", "a2b1c5a3"),

    # 2. No repeats: compressed is longer
    ("abc", "abc"),

    # 3. Empty string
    ("", ""),

    # 4. Single character
    ("a", "a"),

    # 5. Compressed is the same length
    ("aa", "aa"),

    # 6. Simple run
    ("aaa", "a3"),

    # 7. Same length again
    ("aabb", "aabb"),

    # 8. Just shorter
    ("aaabb", "a3b2"),

    # 9. Count with two digits
    ("a" * 12, "a12"),

    # 10. Case-sensitive
    ("aaaAAA", "a3A3"),

    # 11. Two-digit count in the middle
    ("a" + "b" * 10 + "c", "a1b10c1"),

    # 12. Same letter in separate runs
    ("aaabbbaaa", "a3b3a3"),

    # 13. Only one short run
    ("abcdd", "abcdd"),

    # 14. Long run at the end
    ("abbbbb", "a1b5"),

    # 15. Long run at the start
    ("aaaaab", "a5b1"),
]

for i, (s, expected) in enumerate(tests, 1):
    result = compress(s)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected!r}, got {result!r}")
