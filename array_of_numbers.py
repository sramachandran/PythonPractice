list_numbers = [10, 78, 23, 45, 67]

highest_3 = list_numbers[0]*list_numbers[1] * list_numbers[2]

highest = max(list_numbers[0],list_numbers[1])
lowest = min(list_numbers[0], list_numbers[1])
highest_2 = list_numbers[0]*list_numbers[1]
lowest_2 = list_numbers[0]*list_numbers[1]

for i in range(2,len(list_numbers)-1):
    current = list_numbers[2]

    highest_3 = max(highest_3, highest_2 * current, lowest_2 * current)

    highest_2 = max(highest_2, current*highest, current*lowest)

    lowest_2 = min(highest_2, current*highest, current*lowest)

    highest= max(highest,current)

    lowest=min(lowest,current)

print(highest_3)