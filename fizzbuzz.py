numbers = [10, 25, 30, 42, 60]
for i,num in enumerate(numbers):
    if num%5==0 and num%3==0:
        print('fizzbuzz')
    elif num%3==0:
        print('fizz')
    elif num%5==0:
        print('buzz')
    print(i, num)

