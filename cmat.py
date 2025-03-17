from typing import List
import itertools

def solve(n:int, bill_levels: List[int], bob_levels: List[int]) -> str:
    print("The level is %d" % n)
    
    print("bill can do these levels:", " ".join(map(str, bill_levels)))

    print("bob can do these levels:", " ".join(map(str, bob_levels)))

n = 5

bill_levels = [3, 1, 2, 3]

bob_levels = [2, 2, 4]

solve(n, bill_levels, bob_levels)
