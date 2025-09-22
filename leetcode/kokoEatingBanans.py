def eatingSpeed(piles: list[int], h: int) -> int:
    minSpeed = 1
    maxSpeed = max(piles)
    while minSpeed <= maxSpeed:
        m = (maxSpeed + minSpeed) // 2
        count = 0
        for i in piles:
            count += (i + m - 1) // m 
        if count > h:
            minSpeed = m + 1
        elif count <= h:
            maxSpeed = m - 1
    return minSpeed

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
