import pandas

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

df = pandas.DataFrame(dict)

df.index = ["BR", "RU", "IN", "CH", "SA"]

cars = pandas.read_csv('cars.csv', index_col = 0)

print(cars['cars_per_cap'])

print(cars[0:4])


