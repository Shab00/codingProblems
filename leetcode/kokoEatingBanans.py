def eatingSpeed(piles: list[int], h: int) -> int:
    pass

inputs = [([3,6,7,11], 8, 4),
          ([30,11,23,4,20], 5, 30),
          ([30,11,23,4,20], 6, 23)]

for i, h, e in inputs:
    result = eatingSpeed(i, h)
    print(
            f"inputs:\n{i, h}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
