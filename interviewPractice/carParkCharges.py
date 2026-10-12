from collections import defaultdict

def to_minutes(t):
    # "09:30" -> 570
    ...
    mins = (int(t[:2]) * 60) + int(t[3:])
    return mins

def visit_cost(minutes):
    # apply the free 15 minutes and the 3-per-started-hour rule
    ...
    if minutes <= 15:
        return 0
    return 3 * ((minutes + 59) // 60)

def solution(P, T, A):
    parked = {}                  # plate -> entry time in minutes
    fees = defaultdict(int)      # plate -> total fees so far
    # Loop 1: go through events in order
    for plate, time, action in zip(P, T, A):
        if action == "ENTER":
            parked[plate] =  to_minutes(time)
        else:
            fees[plate] += visit_cost(to_minutes(time) - parked[plate])
            del parked[plate]

    # Loop 2: cars still parked at the end of the day
    for car in parked.keys():
        fees[car] += visit_cost(1440 - parked[car])

    # Loop 3: apply the daily cap per car and add up
    for key, charge in fees.items():
        cap = min(20, charge)
        fees[key] = cap

    return sum(fees.values())

        

GREEN, RED, RESET = "\033[92m", "\033[91m", "\033[0m"

tests = [
    # (P, T, A, expected)

    # 1. Basic 90-minute visit
    (["AB12", "AB12"], ["09:00", "10:30"], ["ENTER", "EXIT"], 6),

    # 2. Exactly 15 minutes is free
    (["CD34", "CD34"], ["12:00", "12:15"], ["ENTER", "EXIT"], 0),

    # 3. Never exits
    (["GH78"], ["22:30"], ["ENTER"], 6),

    # 4. 16 minutes is no longer free
    (["J1", "J1"], ["10:00", "10:16"], ["ENTER", "EXIT"], 3),

    # 5. Exactly 60 minutes
    (["K2", "K2"], ["10:00", "11:00"], ["ENTER", "EXIT"], 3),

    # 6. 61 minutes
    (["L3", "L3"], ["10:00", "11:01"], ["ENTER", "EXIT"], 6),

    # 7. Two visits by the same car hit the cap
    (["EF56"] * 4,
     ["00:00", "05:00", "06:00", "08:01"],
     ["ENTER", "EXIT", "ENTER", "EXIT"],
     20),

    # 8. Two cars interleaved
    (["A1", "B2", "A1", "B2"],
     ["08:00", "08:30", "09:00", "11:00"],
     ["ENTER", "ENTER", "EXIT", "EXIT"],
     12),

    # 9. Cap is per car, not for the whole car park
    (["X1", "Y2"], ["00:00", "00:00"], ["ENTER", "ENTER"], 40),

    # 10. Free short visit, then a paid one
    (["Z9"] * 4,
     ["10:00", "10:10", "11:00", "13:30"],
     ["ENTER", "EXIT", "ENTER", "EXIT"],
     9),

    # 11. Enters one minute before midnight
    (["M4"], ["23:59"], ["ENTER"], 0),
]

for i, (P, T, A, expected) in enumerate(tests, 1):
    result = solution(P, T, A)
    if result == expected:
        print(f"Test {i}: {GREEN}PASS{RESET}")
    else:
        print(f"Test {i}: {RED}FAIL{RESET}  expected {expected}, got {result}")
