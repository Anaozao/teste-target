def reverse_string():
    string = str(input("Digite sua string: "))
    reversed_chars = []
    for char in string:
        reversed_chars.insert(0, char)

    reversed_string = "".join(reversed_chars)
    return reversed_string


print(reverse_string())
