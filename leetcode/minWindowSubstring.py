def minWindow(s: str, t: str) -> str:
    pass

inputs = [("OUZODYXAZV", "XYZ", "YXAZ"),
          ("xyz", "xyz", "xyz"),
          ("x", "xy", "")]

for i, o, e in inputs:
    result = minWindow(i, o)
    print(
            f"inputs:\n{i, o}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
