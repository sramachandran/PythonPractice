num=int(input("Enter a number:"))
if num%2==0 and num%4>0:
    print("It's a even number")
if num%2>0 and num%4>0:
    print("Its a odd number")
if num%4==0:
    print("It's divisible by 4")