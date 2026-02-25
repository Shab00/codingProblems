# Binary search practice utilities and checks
# Templates: lower_bound (first >= target), upper_bound (first > target)
# Helpers: find_exact, count_occurrences, insert_position, floor_sqrt, rotated_search

from typing import List

def lower_bound(a: List[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (hi + lo) // 2

        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(a: List[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (hi + lo) // 2

        if a[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def find_exact(a: List[int], target: int) -> int:
    idx = lower_bound(a, target)
    if idx < len(a) and a[idx] == target:
        return idx
    return -1

def count_occurrences(a: List[int], target: int) -> int:
    return upper_bound(a, target) - lower_bound(a, target)

def insert_position(a: List[int], target: int) -> int:
    return lower_bound(a, target)

def floor_sqrt(n: int) -> int:
    lo, hi = 0, n + 1
    while lo < hi:
        mid = (hi + lo) // 2
        if mid * mid <= n:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

def search_rotated(a: List[int], target: int) -> int:
    # search in rotated sorted array (no duplicates assumed)
    lo, hi = 0, len(a) 
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        # left half sorted?
        if a[lo] <= a[mid]:
            if a[lo] <= target < a[mid]:
                hi = mid
            else:
                lo = mid + 1
        else:
            # right half sorted
            if a[mid] < target <= a[hi - 1]:
                lo = mid + 1
            else:
                hi = mid
    return -1

# ---------- Quick checks (print results) ----------
if __name__ == "__main__":
    a = [1, 2, 2, 3, 5]
    print("Array:", a)
    t = 2
    print(f"lower_bound(a, {t}) ->", lower_bound(a, t))   # expect 1
    print(f"upper_bound(a, {t}) ->", upper_bound(a, t))   # expect 3
    print(f"find_exact(a, {t}) ->", find_exact(a, t))     # expect 1
    print(f"count_occurrences(a, {t}) ->", count_occurrences(a, t))  # expect 2
    t2 = 4
    print(f"insert_position(a, {t2}) ->", insert_position(a, t2))    # expect 4 (before 5)

    print("\nFloor sqrt checks:")
    for n in [0, 1, 2, 3, 4, 15, 16, 17, 10**9]:
        print(f"floor_sqrt({n}) = {floor_sqrt(n)}")

    print("\nRotated-array search checks:")
    r = [4,5,6,7,0,1,2]
    print("Rotated array:", r)
    print("search_rotated(r, 0) ->", search_rotated(r, 0))  # expect 4
    print("search_rotated(r, 3) ->", search_rotated(r, 3))  # expect -1

    # Edge cases
    print("\nEdge cases:")
    empty = []
    print("lower_bound([], 5) ->", lower_bound(empty, 5))  # expect 0
    one = [10]
    print("lower_bound([10], 10) ->", lower_bound(one, 10))  # expect 0
    print("upper_bound([10], 10) ->", upper_bound(one, 10))  # expect 1
