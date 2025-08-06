def longComPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    shortest_word = min(strs, key=len)
    
    for i in range(len(shortest_word)):
        char = shortest_word[i]
        for word in strs:
            if word[i] != char:
                return shortest_word[:i]
    return shortest_word

inputs = [(["flower","flow","flight"], "fl"), 
          (["dog","racecar","car"],"")]

for i, e in inputs:
    result = longComPrefix(i)
    print(f"inputs: {i} || outputs: {result} || expected: {e}")
