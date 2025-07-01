def subsets(s: list) -> list[list]:
    result = []

    def dfs(index, current):
        if index == len(s):
            result.append(current[:]) 
            return
        current.append(s[index])
        dfs(index + 1, current)
        current.pop()
        dfs(index + 1, current)

    dfs(0, [])
    return result



print(subsets([1,2]))
