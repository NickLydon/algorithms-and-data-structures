def min_n2(lst):
    if len(lst) == 0:
        return None

    minimum = lst[0]

    for x in lst:
        for x2 in lst:
            if x <= x2 and x <= minimum:
                minimum = x

    return minimum


def min_n(lst):
    if len(lst) == 0:
        return None

    minimum = lst[0]

    for x in lst:
        if x <= minimum:
            minimum = x

    return minimum


print(min_n2([1, 2, 3, 4, 5]))
print(min_n([5]))
