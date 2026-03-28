def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
num = int(input("Enter number: "))
result = check_even_odd(num)
print(f"The number is: {result}")