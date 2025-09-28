def maxProfit(prices: list[int]) -> int:
    pass

inputs = [([7,1,5,3,6,4], 5),
          ([7,6,4,3,1], 0)]

for i, e in inputs:
    result = maxProfit(i)
    print(
            f"inputs:\n{i}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
