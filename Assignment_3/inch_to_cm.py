while True:
    inches = float(input("Enter inches (negative value to stop): "))
    if inches < 0:
        print("Program ended.")
        break
    cent = inches * 2.54
    print(f"{inches} inches = {cent:.2f} centimeters")
