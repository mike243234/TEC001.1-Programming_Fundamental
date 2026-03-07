
numbers = []

while True:
    num = input("Enter a number (press Enter to stop): ")
    if num == "":
        break
    numbers.append(float(num))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for n in numbers[:5]:
    print(n)
