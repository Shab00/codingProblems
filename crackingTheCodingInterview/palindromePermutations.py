from collections import defaultdict

def is_palindrome_permutation(s: str) -> bool:
    hmap = defaultdict(int)
    count_map = defaultdict(int)
    s = s.lower()

    for letter in s:
        if letter != " ":
            hmap[letter] += 1
    
    for letter, count in hmap.items():
        if hmap[letter] % 2 == 0:
            count_map['even'] += 1
        else:
            count_map['odd'] += 1 
   
    
    return count_map['odd'] <= 1

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (s, expected)

    # 1. Book example
    ("Tact Coa", True),

    # 2. Empty string
    ("", True),

    # 3. Single character
    ("a", True),

    # 4. Two different characters
    ("ab", False),

    # 5. Two of the same
    ("aa", True),

    # 6. Odd length
    ("aab", True),

    # 7. All different
    ("abc", False),

    # 8. Even length
    ("aabb", True),

    # 9. Odd length, longer
    ("aabbc", True),

    # 10. Even length, longer
    ("aabbcd", False),

    # 11. Case is ignored
    ("Aa", True),

    # 12. Already a palindrome
    ("racecar", True),

    # 13. Same letters, with a space
    ("car race", True),

    # 14. Repeated pattern
    ("abcabc", True),

    # 15. Repeated pattern plus one
    ("abcabcd", True),

    # 16. Three of each
    ("aaabbb", False),

    # 17. Only spaces
    ("   ", True),

    # 18. A normal phrase
    ("Hello World", False),
]

for i, (s, expected) in enumerate(tests, 1):
    result = is_palindrome_permutation(s)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
