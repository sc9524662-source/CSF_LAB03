#displaying the menu
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# taking choice as input
choice = int(input("Enter choice: "))
num1, num2 = map(int, input("Enter two numbers: ").split())
#Logic using if-elif
if choice == 1:
    res = num1 + num2
    print(f"Sum = {res}")
elif choice == 2:
    res = num1 - num2
    print(f"Difference = {res}")
elif choice == 3:
    res = num1 * num2
    print(f"Product = {res}")
elif choice == 4:
    if num2 != 0:
        res = num1/num2
        print(f"Quotient = {res}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Choice")

    