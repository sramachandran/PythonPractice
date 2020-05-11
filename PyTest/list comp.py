def count_vowels(txt):
	vowels = ['a','e','i','o','u']
	count=0
	return sum([1 for i in txt if i in vowels])


print(count_vowels('aeroplane'))