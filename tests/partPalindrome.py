def pal_partitions(s: str) -> list[list[str]]:
    """
    Return all possible palindrome partitionings of s.
    Each partition is a list of substrings such that every substring is a palindrome.
    Example:
        s = "aab" -> [["a","a","b"], ["aa","b"]]

    Hints (keep these comments while you implement):
    - Backtracking approach:
        res = []
        cur = []
        def dfs(start):
            # if start == len(s): append a COPY of cur to res and return
            # for end in range(start, len(s)):
            #     # if s[start:end+1] is a palindrome:
            #         # choose: cur.append(s[start:end+1])
            #         # recurse: dfs(end+1)
            #         # undo: cur.pop()
    - Palindrome check options:
        - Simple two-pointer check each time (O(len) per check).
        - Or precompute a DP table is_pal[i][j] indicating s[i:j+1] is palindrome (O(n^2) preprocess).
    - Make sure to append a COPY of cur (res.append(cur[:])) when recording a full partition.
    - Return res.
    """
    # TODO: implement this function using backtracking as described above
    res = []
    cur = []
    def dfs(start):
        if start == len(s):
            res.append(cur[:])
            return 
        for end in range(start, len(s)):
            if isPal(s, start, end):
                cur.append(s[start: end+1])
                dfs(end+1)
                cur.pop()
    dfs(0)
    return res
def isPal(s,i,j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# ======= Checker and tests (do NOT modify) =======
from collections import Counter

tests = [
    ("aab", [["a","a","b"], ["aa","b"]]),
    ("a",   [["a"]]),
    ("",    [[]])  # empty string -> one partition: empty list
]

def is_valid_partition_for_input(partition, s):
    # partition must be a list/tuple of strings
    if not isinstance(partition, (list, tuple)):
        return False
    # pieces must concatenate to s
    if "".join(partition) != s:
        return False
    # each piece must be a palindrome
    for piece in partition:
        if piece != piece[::-1]:
            return False
    return True

def check_pal_partitions(s, expected):
    try:
        result = pal_partitions(s)
    except Exception as e:
        print(f"ERROR calling pal_partitions({s!r}): {e}")
        return False

    if not isinstance(result, list):
        print("ERROR: pal_partitions must return a list")
        return False

    # basic validity checks
    for p in result:
        if not is_valid_partition_for_input(p, s):
            print("FAIL - invalid partition returned:", p)
            return False

    # compare as multisets of tuples so outer order doesn't matter
    res_count = Counter(tuple(p) for p in result)
    exp_count = Counter(tuple(p) for p in expected)

    if res_count == exp_count:
        print("PASS")
        return True
    else:
        print("FAIL")
        print(" expected (any order):", sorted([tuple(s) for s in expected]))
        print(" got      (any order):", sorted([tuple(s) for s in result]))
        missing = list((exp_count - res_count).elements())
        unexpected = list((res_count - exp_count).elements())
        if missing:
            print(" MISSING partitions:", missing)
        if unexpected:
            print(" UNEXPECTED partitions:", unexpected)
        return False

# Run tests
if __name__ == "__main__":
    for s, expected in tests:
        print("s =", repr(s))
        check_pal_partitions(s, expected)
        print()
