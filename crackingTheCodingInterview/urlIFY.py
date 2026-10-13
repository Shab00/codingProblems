def urlify(chars: list, true_length: int) -> None:
    r = len(chars) - 1
    l =  true_length - 1
    
    while l >= 0:
        if chars[l] == " ":
            chars[r] = "0"
            r -= 1 
            chars[r] = "2"
            r -= 1
            chars[r] = "%"
            l -= 1
            r -= 1
        else:
            chars[r] = chars[l] 
            l -= 1
            r -= 1

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

def make_buffer(text: str) -> list:
    return list(text) + [" "] * (2 * text.count(" "))

tests = [
    ("Mr John Smith", 13, "Mr%20John%20Smith"),
    ("hello", 5, "hello"),
    ("", 0, ""),
    (" ", 1, "%20"),
    (" a", 2, "%20a"),
    ("a ", 2, "a%20"),
    ("a  b", 4, "a%20%20b"),
    ("   ", 3, "%20%20%20"),
    ("a b c d", 7, "a%20b%20c%20d"),
    (" hi ", 4, "%20hi%20"),
    ("100% sure", 9, "100%%20sure"),
]

for i, (text, true_length, expected) in enumerate(tests, 1):
    chars = make_buffer(text)
    urlify(chars, true_length)
    result = "".join(chars)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected!r}, got {result!r}")
