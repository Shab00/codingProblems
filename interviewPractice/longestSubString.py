def lengthOfLongestSubstring(s: str) -> int:
    lastIndex = {}
    left, best = 0, 0

    for right, ch in enumerate(s):
        if ch in lastIndex and lastIndex[ch] >= left:
            left = lastIndex[ch] + 1
        lastIndex[ch] = right
        best = max(best, (right - left + 1))
    return best
if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
    print(lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
    print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
    print(lengthOfLongestSubstring(""))          # 0
