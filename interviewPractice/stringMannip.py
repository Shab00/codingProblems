def StringChallenge(strParam, num):
    result = []

    for char in strParam:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift = chr((ord(char) - start + num) % 26 + start)
            result.append(shift)
        else:
            result.append(char)

    shift = "".join(result)

    token = "3xtd4e9iyf10?"
    final_result = []

    for char in shift:
        if char.lower() in token:
            final_result.append(f"--{char}--")
        else:
            final_result.append(char)

    return "".join(final_result)
