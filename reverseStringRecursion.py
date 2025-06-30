def reverse_string(word: str) -> str:
    if len(word) < 1:
        return word

    return word[::-1]

print(reverse_string("hello"))
print(reverse_string("recursion"))
print(reverse_string(""))
