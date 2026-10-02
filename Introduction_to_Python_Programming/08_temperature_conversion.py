choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice == "C":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

elif choice == "F":
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Celsius =", celsius)

else:
    print("Invalid choice")