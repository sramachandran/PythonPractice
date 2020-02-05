list_a = ["a", "b", "c", "d", "e", "f", "g"]

list_length = len(list_a)

left_index=0

right_index=len(list_a)-1

while left_index<right_index:
    list_a[left_index], list_a[right_index] = list_a[right_index], list_a[left_index]

    left_index += 1
    right_index -= 1

print(list_a)