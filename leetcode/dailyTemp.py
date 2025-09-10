def dailyTemp(temp: list[int]) -> list[int]:
    l = []
    for i in range(len(temp)):
        p = i + 1
        count = 0
        while p < len(temp):
            if temp[i] < temp[p]:
                count += 1
                l.append(count)
                count = 0
                p += 1
                break
            else:
                count += 1
                p += 1
        else:
            l.append(0)
    return l

inputs = [([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
          ([30,40,50,60], [1,1,1,0]),
          ([30,60,90], [1,1,0])
          ]

for i, e in inputs:
    result = dailyTemp(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
