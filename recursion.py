def palindrome(s1):
    if len(s1) < 2:
        return True
    elif s1[0] != s1[-1]:
        return False
    else:
        return palindrome(s1[1:-1])


def reverse(s1):
    if len(s1) == 0:
        return ''
    else:
        return s1[-1] + reverse(s1[:-1])


words = ["mada", "madam", "", "m"]
for word in words:
    print(word + " is a palindrome: " + str(palindrome(word)))
    print(word + " backwards is: " + reverse(word))
