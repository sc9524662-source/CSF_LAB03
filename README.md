# csf_Lab03
# Aim of the lab
To build a clear and practical understanding of control structures in Python by working with conditions, loops, and statements like break and continue, and by learning how to create and use functions to solve problems in a more organized and efficient way.
# List of programs and brief explanation of each task
1.Program Name: Positive, Negative, or Zero Checker
This program takes a number as input from the user using input() and converts it into a float using float(). It then uses conditional statements (if,elif,else) to check whether the number is greater than zero, less than zero, or equal to zero. Based on the condition, it prints whether the number is positive, negative, or zero.

2.Program name: Even and Odd Number Checker
This program asks the user to enter a number and converts it into an integer. It then checks whether the number is divisible by 2 using the modulus operator %. If the remainder is 0, it prints that the number is even; otherwise, it prints that the number is odd.

3.Program name: Largest of Two Numbers Finder
This program takes two integer inputs from the user and compares them using conditional statements (if, elif, else). It checks which number is greater and prints the larger number. If both numbers are equal, it displays that they are equal.

4.Program name: Largest of Three Numbers Finder
This program compares three numbers (num1, num2, and num3) to find the largest among them. It uses nested if-else statements to first compare two numbers and then compare the result with the third number. Finally, it stores the largest value in the variable largest and displays it as output.

5.Program name: Student Grade Calculator
This program takes the student’s marks as input and assigns a grade based on the marks using nested if-else statements. It checks different conditions: marks greater than or equal to 80 get grade A, 60–79 get grade B, 40–59 get grade C, and below 40 is marked as Fail. Finally, it displays the corresponding grade.

6.Program name: Simple Menu-Driven Calculator
This program displays a menu of basic arithmetic operations: addition, subtraction, multiplication, and division. The user selects an option and enters two numbers. Based on the chosen option, the program performs the corresponding operation using if-elif statements and displays the result. It also includes error handling for division by zero and invalid choices.

7.Program name: Print Numbers from 1 to 10 Using Loop
This program uses a for loop with the range() function to print numbers from 1 to 10. The loop runs from 1 up to 10 (inclusive of 1 and exclusive of 11), and each number is displayed using print(). The end="" parameter is used to print the numbers in a single line without line breaks

8.Program name: Printing Even Numbers from 1 to 20 Using Loop
This program uses a for loop with the range() function to print all even numbers between 1 and 20. The range(2, 21, 2) starts from 2 and increases by 2 in each step, ensuring only even numbers are generated. The print() function displays the numbers in a single line using end="".

9.Program name: Sum of Numbers from 1 to 10
This program calculates the cumulative sum of numbers from 1 to 10 using a for loop. It starts with total_sum initialized to 0, then adds each number from 1 to 10 one by one. After each addition, it prints the current sum, showing how the total increases step by step.


10.Program name: Multiplication Table Generator
This program takes a number as input from the user and generates its multiplication table from 1 to 10. It uses a for loop to iterate through numbers 1 to 10 and multiplies each value with the given number. The result is displayed in a formatted way showing the multiplication expression and its output.

11.Program name: Print Numbers from 1 to 5 Using While Loop
This program uses a while loop to print numbers from 1 to 5. It starts with i = 1 and continues looping as long as i is less than or equal to 5. In each iteration, it prints the value of i and then increases it by 1 using i += 1, ensuring the loop eventually stops.

12.Program name: Sum of First n Natural Numbers Using While Loop
This program calculates the sum of the first n natural numbers using a while loop. It takes a number n as input from the user, then adds all numbers from 1 to n one by one using a loop. The variable sum_total stores the running total, and finally the program displays the total sum.

13.Program name: Break Statement in While Loop
This program uses an infinite while loop to repeatedly take a number as input from the user. If the user enters 0, the program prints “Loop ended” and stops the loop using the break statement. Otherwise, it continues asking for numbers.

14.Program Name:Break Statement in For Loop
This program uses a for loop to print numbers from 1 to 10. However, when the value of i becomes 6, the break statement stops the loop immediately. As a result, only numbers from 1 to 5 are printed.

15.Program name:Continue Statement in For Loop
This program uses a for loop to print numbers from 1 to 10. When the loop reaches the value 5, the continue statement skips that iteration and does not print 5. The loop then continues normally with the remaining numbers.

16.Program name:Linear Search in a List
This program searches for a specific number in a list using a for loop. It checks each element in the list one by one until it finds the target value. If the number is found, it prints “Number found” and stops the loop using the break statement. If the number is not found, the loop continues until all elements are checked.

17.Program name:Function to Print Hello World
This program defines a function named say_hello() that prints “Hello, World!” when called. The function contains a print() statement, but it will only display the message when the function is invoked. It helps demonstrate how functions are defined and used in Python.

18.Program name:Square of a Number Using Function Logic
This program takes a number as input from the user and calculates its square by multiplying the number by itself (n * n). It then displays the result using the print() function. This program demonstrates a simple arithmetic operation in Python.

19.Program name:Function to Add Two Number
This program defines a function add_numbers(a, b) that takes two parameters and returns their sum. The user inputs two numbers, which are converted into integers. The function is then called with these values, and the returned result (sum) is displayed as output.

20.Program name:Even or Odd Checker Using Function
This program defines a function check_even_odd(n) that checks whether a number is even or odd using the modulus operator %. If the number is divisible by 2, it returns "even"; otherwise, it returns "odd". The user inputs a number, the function is called with that value, and the result is displayed as output.

21.Program name:Factorial of a Number
This program calculates the factorial of a given number entered by the user. It uses a for loop to multiply all numbers from 1 up to the given number. The variable fact is initialized to 1 and is updated in each iteration of the loop. Finally, the program displays the factorial result.

22.Program name:Multiplication Table Using format() Method
This program takes a number as input from the user and prints its multiplication table from 1 to 10. It uses a for loop to iterate through values 1 to 10 and multiplies each value with the given number. The format() method is used to display the output in a structured and readable format.

23.Program name: Even and Odd Number Checker (Using Loop)
This program takes a number n from the user and uses a for loop to go through all numbers from 1 to n. For each number, it checks whether it is divisible by 2 using the modulus operator %. If the remainder is 0, the number is even; otherwise, it is odd. It then prints each number along with whether it is even or odd.

24.Program name: Menu-Driven Calculator Using Loop
This program creates a simple calculator that repeatedly shows a menu of operations: addition, subtraction, multiplication, division, and exit. It uses a while True loop to keep the program running until the user chooses to exit. Based on the user’s choice, it takes two numbers as input and performs the selected operation. It also includes a condition to handle division by zero and displays an error message if the user enters an invalid option.