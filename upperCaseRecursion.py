def count_uppercase(word: str) -> int:
    
    if word == "":
        return 0
    count = 1
    if word[0].isupper():
        return count + count_uppercase(word[1:])
    else:
        
        return count_uppercase(word[1:])


print(count_uppercase("HelloWorld") )
print(count_uppercase("PYTHON")   )
print(count_uppercase("abc") )
print(count_uppercase(""))
