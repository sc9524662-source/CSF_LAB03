# program to find the largest of three numbers using nested if-else
num1 =5
num2 = 9
num3 = 3
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
    print("The largest number is",largest)