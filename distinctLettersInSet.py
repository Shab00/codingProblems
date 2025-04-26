def solve(set_str:str) -> int:
        print(f"set_str: {set_str}")

        count = []

        for i in set_str:
            if i not in set_str:
                count.append(i)

        return len(set_str)


inputs = {'b', 'a', 'b', 'a'}

result = solve(inputs)

print(result)
