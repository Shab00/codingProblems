def genPar(n: int) -> list[str]:
    if not n:
        return []
    
    ret = []

    def backtrack(left, right, curString):

        if len(curString) == 2 * n:
            ret.append(curString)
            return
   
        if left < n:
            backtrack(left+1, right, curString + "(")
        if right < left:
            backtrack(left, right, curString + ")")
    backtrack(0, 0, "")
    return ret


inputs = [(1, ["()"]),
          (2, ["(())","()()"]),
          (3, ["((()))","(()())","(())()","()(())","()()()"]),
          (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])]

for i, o in inputs:
    result = genPar(i)
    print(f"input: {i} || output: {result} || ecpected: {o}")
