print("hi")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_numbers = list(set(list1) ^ set(list2))
print(unique_numbers)
