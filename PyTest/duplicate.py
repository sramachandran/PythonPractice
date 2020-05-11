x = [1,2,3,4,4,5,6,6,6,6,7]
s = set()
for i in x:
    if i not in s:
        s.add(i)
l=list(s)
print(l)