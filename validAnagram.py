def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    return sorted(s) == sorted(t)

inputs = [("anagram", "nagaram"),
          ("rat", "cat")]

for i in inputs:
    print(i)
    results = solve(*i)
    print(results)
