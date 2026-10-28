def check_permutation(s1: str, s2: str) -> bool:

    h1 = {}
    h2 = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i not in h1:
            h1[i] = 0
        h1[i] += 1

    for j in s2:
        if j not in h2:
            h2[j] = 0
        h2[j] += 1

    return h1 == h2

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (s1, s2, expected)

    # 1. Simple rearrangement
    ("abc", "bca", True),

    # 2. Same length, different letters
    ("abc", "abd", False),

    # 3. Different lengths
    ("abc", "abcd", False),

    # 4. Two empty strings
    ("", "", True),

    # 5. One empty, one not
    ("", "a", False),

    # 6. Repeated letters, same counts
    ("aabb", "abab", True),

    # 7. Same set of letters but different counts
    ("aab", "abb", False),

    # 8. Case-sensitive
    ("Dog", "god", False),

    # 9. Whitespace counts
    ("god ", "dog", False),

    # 10. Spaces in both, still a permutation
    ("a b", "b a", True),

    # 11. Classic anagram
    ("listen", "silent", True),

    # 12. Identical strings
    ("a", "a", True),

    # 13. Same letters, counts swapped
    ("aaab", "abbb", False),

    # 14. Digits and symbols
    ("12!3", "3!21", True),
]

for i, (s1, s2, expected) in enumerate(tests, 1):
    result = check_permutation(s1, s2)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
