x=input("Enter a string:")
y=input("Enter another string:")
j=""
z=[]
for i in x:
    if i in y:
        z.append(i)
print(z)

