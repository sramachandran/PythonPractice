num=int(input("Enter your number:"))
lis=list(range(1,num+1))
div=0
x=[]
for i in lis:
    if num%i==0:
        div=i
        x.append(div)
print(x)