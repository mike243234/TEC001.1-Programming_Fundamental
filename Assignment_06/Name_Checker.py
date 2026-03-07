
names = []

while True:
    name = input("Enter a name (press Enter to stop): ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.append(name)

print("Names entered:")
for n in names:
    print(n)
