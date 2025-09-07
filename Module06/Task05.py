def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]


my_list = [1, 2, 3, 4, 5, 6, 7]
filtered_list = remove_odds(my_list)

print("Original list:", my_list)
print("Even numbers only:", filtered_list)
