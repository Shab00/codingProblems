def one_away(s1: str, s2: str) -> bool:
    
    s1 = s1.lower()
    s2 = s2.lower()

    count = 0 

    lenDiff = abs(len(s1) - len(s2))

    if lenDiff > 1:
        return False
    
    if len(s1) == len(s2):

        for p1, p2 in zip(s1, s2):
            if p1 != p2:
                count += 1

        return count <= 1

    else:

        if len(s1) > len(s2):
            longer, shorter = s1, s2
        else:
            longer, shorter = s2, s1

        i, j = 0, 0
        diff = 0

        while j < len(shorter):

            if longer[i] == shorter[j]:
                i += 1
                j += 1
            else:
                diff += 1
                i += 1
            if diff > 1:
                return False

        return True 

            


        

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (s1, s2, expected)

    # 1. Book example: remove
    ("pale", "ple", True),

    # 2. Book example: insert
    ("pales", "pale", True),

    # 3. Book example: replace
    ("pale", "bale", True),

    # 4. Book example: two replaces
    ("pale", "bake", False),

    # 5. Identical strings (zero edits)
    ("pale", "pale", True),

    # 6. Both empty
    ("", "", True),

    # 7. Empty and one character
    ("", "a", True),

    # 8. One character and empty
    ("a", "", True),

    # 9. Empty and two characters
    ("", "ab", False),

    # 10. Single character replaced
    ("a", "b", True),

    # 11. Swapped characters
    ("ab", "ba", False),

    # 12. Last character removed
    ("pale", "pal", True),

    # 13. First character removed
    ("pale", "ale", True),

    # 14. Length differs by 2
    ("pale", "palesx", False),

    # 15. Middle character removed
    ("apple", "aple", True),

    # 16. Middle character replaced
    ("abc", "axc", True),

    # 17. Two replaces, far apart
    ("abcd", "axcy", False),

    # 18. Character inserted in the middle
    ("abc", "abxc", True),

    # 19. Length differs by 1 but also a replace
    ("abc", "xbcd", False),

    # 20. Case-sensitive replace
    ("Pale", "pale", True),
]

for i, (s1, s2, expected) in enumerate(tests, 1):
    result = one_away(s1, s2)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
