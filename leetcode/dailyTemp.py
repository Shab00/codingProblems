def dailyTemp(temp: list[int]) -> list[int]:
    pass

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
