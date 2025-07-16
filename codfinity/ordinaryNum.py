def solve(n:int) -> int:
    string = str(n)
    digLen = len(str(n))
    all_same = all(ch == string[0] for ch in string)
    dif = 9 - int(string[0])
    if all_same:
        return (digLen * 9) - dif - 1 
    else:
        return (digLen * 9) - dif - 1 

def best(n: int) -> int:
        string = str(n)
        digLen = len(string)
        first_digit = int(string[0])
        candidate = int(string[0] * digLen)
        
        count = (digLen - 1) * 9
        
        if candidate <= n:
            count += first_digit
        else:
            count += first_digit - 1
        
        return count

inputs = [100, 5, 50, 999, 777777, 555]

for i in inputs:
    result = best(i)
    print(result)
