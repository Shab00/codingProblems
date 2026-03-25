from collections import deque

inputs = [("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
          ("hit", "cog", ["hot","dot","dog","lot","log"], 0)]

def ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordset = set(wordList)
    count = 1
    vist = set()

    if endWord not in wordset:
        return 0

    q = deque([(beginWord, count)])
    vist.add(beginWord)    
    while q:
        word, count = q.popleft()
        if word == endWord:
            return count
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != word[i]:
                    new = word[:i] + c + word[i+1:]
                    if new in wordset and new not in vist:
                        vist.add(new)
                        q.append((new, count + 1))
    return 0 

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for idx, (begin, end, wList, expec) in enumerate(inputs, start=1):
    result = ladder(begin, end, wList)
    if result == expec:
        print(f"example: {idx} => {result} => {GREEN}PASS{RESET}")
    else:
        print(f"example: {idx} => {result} => {RED}FAIL{RESET}")
