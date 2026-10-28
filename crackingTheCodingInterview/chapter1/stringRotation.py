def is_substring(s1: str, s2: str) -> bool:
    # Given helper: is s2 anywhere inside s1?
    return s2 in s1


def is_rotation(s1: str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False   

    doubleSrting = s1 + s1

    return is_substring(doubleSrting, s2)

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

# Wrap is_substring to count calls
_calls = 0
_original_is_substring = is_substring

def is_substring(s1: str, s2: str) -> bool:
    global _calls
    _calls += 1
    return _original_is_substring(s1, s2)

tests = [
    # (s1, s2, expected)

    # 1. Book example
    ("waterbottle", "erbottlewat", True),

    # 2. Another rotation
    ("waterbottle", "bottlewater", True),

    # 3. Same string (rotated by zero)
    ("waterbottle", "waterbottle", True),

    # 4. Same letters, not a rotation
    ("waterbottle", "erbottlewta", False),

    # 5. Short, not a rotation
    ("abc", "acb", False),

    # 6. Different lengths
    ("abc", "abcd", False),

    # 7. Both empty
    ("", "", True),

    # 8. Single character, same
    ("a", "a", True),

    # 9. Single character, different
    ("a", "b", False),

    # 10. Repeated characters
    ("aa", "aa", True),

    # 11. Rotated by half
    ("abcd", "cdab", True),

    # 12. Rotated by one from the end
    ("abcd", "dabc", True),

    # 13. One empty, one not
    ("abc", "", False),

    # 14. Repeats, valid rotation
    ("aaab", "abaa", True),

    # 15. Repeats, not a rotation
    ("aaab", "abab", False),

    # 16. Alternating pattern
    ("abab", "baba", True),

    # 17. Case-sensitive, valid
    ("Abc", "bcA", True),

    # 18. Case-sensitive, not a rotation
    ("abc", "bcA", False),

    # 19. A substring, but not a rotation
    ("abc", "bc", False),
]

for i, (s1, s2, expected) in enumerate(tests, 1):
    _calls = 0
    result = is_rotation(s1, s2)
    if _calls > 1:
        print(f"Test {i}: {RED}FAIL{RESET}  called is_substring {_calls} times (max 1)")
    elif result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
