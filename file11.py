<<<<<<< HEAD
# This is from the `master` branch
print("hi")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_numbers = list(set(list1) ^ set(list2))
print(unique_numbers)
=======
# This is from the `dumb` branch
print("hi")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_numbers = list(set(list1) ^ set(list2))
print(unique_numbers)

# Add 100 to each unique number
result = [num + 100 for num in unique_numbers]
print(result)
>>>>>>> dumb
