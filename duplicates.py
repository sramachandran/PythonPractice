#remove duplicates

def remove_duplicates(lst):
    s = set()
    for i in lst:
        if i not in s:
            s.add(i)
    return list(s)

print(remove_duplicates([1,1,2,3,4,5]))