def solve(s:str) -> str:
        print(f"s: {s}")
        l = []
        parts = s.split('+')
        sorted_string = '+'.join(sorted(parts))
        return sorted_string

inputs = "1+3+2+1"
result = solve(inputs)
print(result)
