def factorial(num):
	result = num * factorial(num-1)
	return result

print(factorial(3))