def Reverse_String(s):
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)


if __name__ == "__main__":
    s = input().strip()
    print(Reverse_String(s))