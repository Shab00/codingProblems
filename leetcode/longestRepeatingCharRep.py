def charRep(s: str, k: int) -> int:
    count = {}
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        char = s[right]
        if char not in count:
            count[char] = 0
        count[char] += 1

        max_count = max(max_count, count[char])

        while (right - left + 1) - max_count > k:
            left_char = s[left]
            count[left_char] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

inputs = [("ABAB", 2, 4),
          ("AABABBA", 1, 4)]

for s, k, e in inputs:
    result = charRep(s, k)
    print(
            f"inputs:\n{s, k}\n"
            f"outputs:\n{result}\n"
            f"expected:\n{e}\n"
            f"{'-'*50}"
            )
