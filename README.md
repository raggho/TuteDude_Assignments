# Task 1
Ask the user to enter the first number and convert it to an integer using int()  
a = int(input("Enter the First number: "))

Ask the user to enter the second number and convert it to an integer  
b = int(input("Enter the Second number: "))

Print the result of the addition
print("Addition: ", a + b)        Adds a and b, then prints the result

Print the result of the subtraction
print("Subtraction: ", a - b)     Subtracts b from a, then prints the result

Print the result of the multiplication
print("Multiplication: ", a * b)    Multiplies a and b, then prints the result

Print the result of the division
print("Division: ", a / b)    Divides a by b, then prints the result (returns float)


# Task 2

Prompt the user to enter their first name and store it in the variable 'f_name'
f_name = input("Enter the first name: ")

Prompt the user to enter their second (last) name and store it in the variable 's_name'
s_name = input("Enter the Second name: ")

Use an f-string to display a welcome message including the user's full name
print(f"Hello, {f_name} {s_name}! welcome to the python program.")
