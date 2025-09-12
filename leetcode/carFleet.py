def carFleet(target: int, position: list[int], speed: list[int]) -> int:
     pass

inputs = [(12, [10,8,0,5,3], [2,4,1,1,3], 3),
           (10, [3], [3], 1),
           (100, [0,2,4], [4,2,1], 1)]

for i, j, k, e in inputs:
    result = carFleet(i, j, k)
    print(
            f"inputs:\n{i}\n{j}\n{k}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
