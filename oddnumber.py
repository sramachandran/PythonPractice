def oddNumbers(l, r):
    # Write your code here
    if l%2 == 0:
        i=l+1
    else:
        i=l

    if r%2 == 0:
        j = r
    else:
        j = r+1
    lst = range(i,j,2)
    return lst

x=2
y=21

if x%2 == 0:
    i=x+1
else:
    i=x

if y%2 == 0:
    j = y
else:
    j = y+1
lst = range(i,j,2)
return lst