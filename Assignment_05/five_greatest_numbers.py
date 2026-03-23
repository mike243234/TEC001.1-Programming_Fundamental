
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Invalid input, please enter a number.")

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
print(numbers[:5])
