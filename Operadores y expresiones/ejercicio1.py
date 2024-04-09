
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Menu:")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")

option = int(input("Enter your choice (1-3): "))

if option == 1:
    result = num1 + num2
    print("Sum:", result)
elif option == 2:
    result = num1 - num2
    print("Subtraction:", result)
elif option == 3:
    result = num1 * num2
    print("Multiplication:", result)
else:
    print("Invalid option")