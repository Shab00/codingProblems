def fizzBuzz(length: int) -> list:
    ls = []
    for num in range(1, length + 1):
        if num % 3 == 0 and num % 5 == 0:
            ls.append('FizzBuzz')
        elif num % 3 == 0:
            ls.append('Fizz')
        elif num % 5 == 0:
            ls.append('Buzz')
        else:
            ls.append(num)
    return ls

result = fizzBuzz(100)
print(result)
