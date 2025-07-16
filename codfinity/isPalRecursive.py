def is_palindrome(word: str) -> bool:

    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("a"))
print(is_palindrome(""))
