#Given a list of numbers, write a function that returns a list that...
#Has all duplicate elements removed.
#Is sorted from least to greatest value.


def unique_sort(lst):
    s = set()
    for i in lst:
        if i not in s:
            s.add(i)
    return sorted(s)

print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))