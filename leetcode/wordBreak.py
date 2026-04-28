inputs = [("leetcode", ["leet","code"], True), 
          ("applepenapple", ["apple","pen"], True),
          ("catsandog", ["cats","dog","sand","and","cat"], False)]

def word(s: str, wordDict: list[str]) -> bool:
    wset = set(wordDict)
    memo = {}
    def can_break(start):
        if start == len(s): return True
        if start in memo: return memo[start]
        for end in range(start+1, len(s)+1):
            if s[start:end] in wset and can_break(end):
                memo[start] = True
                return True
        memo[start] = False
        return False
    return can_break(0)

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (s, w, expec) in enumerate(inputs, start=1):
    result = word(s, w)
    if result == expec:
        print(f"example: {idx} => {expec} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {expec} => {result} => {RED}FAIL{RESET}")
