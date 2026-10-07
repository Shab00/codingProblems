from collections import defaultdict

def solution(W, D, H):
    daily_hours = defaultdict(int)
    for name, date, hours in zip(W, D, H):
        daily_hours[(name, date)] += hours

    result = defaultdict(int)
    days_in_month = defaultdict(int)

    for (name, date), hours in daily_hours.items():
        normal = min(hours, 8)
        overtime = max(hours - 8, 0)
        result[name] += normal * 10 + overtime * 15

        days_in_month[(name, date[:7])] += 1

    for (name, month), days in days_in_month.items():
        if days >= 5:
            result[name] += 50

    return dict(result)

tests = [
    # (W, D, H, expected)

    # 1. Example 1
    (["ana", "ana", "ben"],
     ["2024-03-01", "2024-03-01", "2024-03-02"],
     [6, 4, 8],
     {"ana": 110, "ben": 80}),

    # 2. Example 2
    (["ana"] * 6,
     ["2024-03-01", "2024-03-02", "2024-03-03",
      "2024-03-04", "2024-03-05", "2024-04-10"],
     [8, 8, 8, 8, 8, 9],
     {"ana": 545}),

    # 3. Example 3
    (["ben"] * 6,
     ["2024-05-01", "2024-05-01", "2024-05-01",
      "2024-05-02", "2024-05-03", "2024-05-04"],
     [3, 3, 3, 1, 1, 1],
     {"ben": 125}),

    # 4. Same month name, different years
    (["ana"] * 5,
     ["2023-01-10", "2023-01-11", "2023-01-12",
      "2024-01-10", "2024-01-11"],
     [8, 8, 8, 8, 8],
     {"ana": 400}),

    # 5. Exactly 8 hours split across shifts
    (["cat", "cat"],
     ["2024-02-14", "2024-02-14"],
     [5, 3],
     {"cat": 80}),

    # 6. Interleaved workers, unsorted dates
    (["dan", "eve", "dan", "eve", "dan"],
     ["2024-06-03", "2024-06-03", "2024-06-01", "2024-06-03", "2024-06-03"],
     [4, 10, 2, 2, 6],
     {"dan": 130, "eve": 140}),

    # 7. Bonus earned in two different months
    (["fay"] * 10,
     ["2024-02-01", "2024-02-02", "2024-02-03", "2024-02-04", "2024-02-05",
      "2024-03-01", "2024-03-02", "2024-03-03", "2024-03-04", "2024-03-05"],
     [1] * 10,
     {"fay": 200}),

    # 8. Large overtime on one day
    (["gus", "gus"],
     ["2024-08-08", "2024-08-08"],
     [16, 16],
     {"gus": 440}),

    # 9. Exactly 5 distinct days, with a repeated day
    (["hal"] * 6,
     ["2024-07-01", "2024-07-01", "2024-07-02",
      "2024-07-03", "2024-07-04", "2024-07-05"],
     [2] * 6,
     {"hal": 170}),

    # 10. Single shift
    (["ivy"], ["2024-12-31"], [1], {"ivy": 10}),
]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for i, (W, D, H, expected) in enumerate(tests, 1):
    result = solution(W, D, H)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}")
        print(f"   expected {expected}")
        print(f"   got      {result}")
