def is_unique(string: str) -> bool:
    hashSet= set()
    for letter in string:
        if letter in hashSet:
            return False
        else:
            hashSet.add(letter)
    return True 

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

all_ascii = "".join(chr(i) for i in range(128))

tests = [
    # (s, expected)

    # 1. All different letters
    ("abcdef", True),

    # 2. Repeated letter in the middle
    ("hello", False),

    # 3. Empty string has no duplicates
    ("", True),

    # 4. Single character
    ("a", True),

    # 5. Case-sensitive: 'a' and 'A' are different
    ("aA", True),

    # 6. Spaces count as characters
    ("a b c", False),

    # 7. Full alphabet
    ("abcdefghijklmnopqrstuvwxyz", True),

    # 8. Duplicate is first and last character
    ("abcdefghijklmnopqrstuvwxyza", False),

    # 9. Digits and symbols
    ("!@#$%!", False),

    # 10. Every ASCII character exactly once
    (all_ascii, True),

    # 11. More than 128 chars must contain a repeat (pigeonhole)
    (all_ascii + "a", False),
]

for i, (s, expected) in enumerate(tests, 1):
    result = is_unique(s)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
