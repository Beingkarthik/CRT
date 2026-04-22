# s = "python Programming"
# print(s.capitalize())
# print(s.title())
# s = s.title()
# print(s)
# print(s.replace("on", "ON"))
# print(s)

# def Reverse_string(s):
#     stop = -1 * (len(s) + 1)
#     res = ""
#     for i in range(-1, stop, -1):
#         res += s[i]
#     return res
# print(Reverse_string("abc"))

# s = "abc"
# print("".join(reversed(s)))

# def is_palindrome(s):
#     return Reverse_string(s) == s
# print(is_palindrome("abc"))
# print(is_palindrome("madam"))
def frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d

def Anagrams(s1,s2):
    return frequency_count(s1) == frequency_count(s2)
    

print(Anagrams("Paces", "spacet"))
print(Anagrams("abc", "aabbcc"))
