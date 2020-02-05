fil=open("demofile.txt","r")
count=0
for line in fil:
    print(line.rstrip())
    count=count+1
print(count,"Lines")