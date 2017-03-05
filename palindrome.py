def palindrome(s1, s2):
    if (len(s1) != len(s2)):
        return False
    start = 0
    end = len(s2) - 1

    while start < end:
        if s1[start] != s2[end]:
            return False
        start += 1
        end -= 1

    return True


print(palindrome("DaD", "DaD"))