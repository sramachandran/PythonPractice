def fizzBuzz(n):
    output=''
    for i in range(1,n+1):
    # Write your code here
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0 and i%5>0:
            print('Fizz')
        elif i%5==0 and i%3>0:
            print('Buzz')
        else:
            print(i)



print(fizzBuzz(15))