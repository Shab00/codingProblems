from typing import List
from collections import deque
def solve(beginWord:str, endWord:str, wordList:List[str])->int:

    dictionary = set(wordList)
    path = deque()
    path.append((beginWord, 1))
    visted = set()
    visted.add(beginWord)
    
    while path:
        curWord, step = path.popleft()
        if curWord == endWord:
            return step
        for word in dictionary:
            defrence = 0            
            for a, b in zip(curWord, word):
                if a != b:
                    defrence += 1
                    
            if defrence == 1 and word not in visted:
                path.append((word, step + 1))
                visted.add(word)
    return 0
        
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

result = solve(beginWord, endWord, wordList)

print(result)
