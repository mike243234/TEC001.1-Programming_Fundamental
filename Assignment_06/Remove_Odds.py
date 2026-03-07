
def remove_odd_numbers(numbers):
    new_list = []

    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)

    return new_list


my_list = [1,2,3,4,5,6,7,8,9,10]

result = remove_odd_numbers(my_list)

print("Original list:", my_list)
print("Without odd numbers:", result)
