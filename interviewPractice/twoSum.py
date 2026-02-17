inputs = [([2,7,11,15], 9, [0,1])]

def sum(arr: list[int], target: int) -> list[int]:
   seen = {}

   for i, x in enumerate(arr):
       need = target - x
       if need in seen:
           return [seen[need], i]
       seen[x] = i

for i, j, k in inputs:
    result = sum(i, j)
    print(f"This is result: {result}\nThis is expected: {k}\n")
