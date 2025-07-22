# Task 1
Define a function to calculate factorial  
def factorial(n):  
    If the number is greater than 1, calculate factorial using a loop  
    if n > 1:  
        fact = 1                  Initialise factorial variable to 1  
        for i in range(1, n + 1):        Loop from 1 to n (inclusive)  
            fact *= i            Multiply fact by the current number i  
    else:  
        fact = 1                 If n is 0 or 1, factorial is 1 by definition  

    Return the result as a formatted string  
    return f"Factorial of {n} is : {fact}"  

Ask the user to enter a number, call the function, and print the result  
print(factorial(int(input("Enter the number: "))))  
 


# Task 2

Import the math module to access mathematical functions  
import math  

Define a function that performs square root, log, and sine operations  
def Calc(n):  
    squrt = math.sqrt(n)      Calculate square root of n  
    loga = math.log(n)        Calculate natural logarithm (base e) of n  
    sine = math.sin(n)        Calculate sine of n (n in radians)  
    
    Return the results as a formatted string  
    return f"Square root: {squrt} \nLogarithm: {loga} \nSine: {sine}"  

Get input from the user, convert it to an integer, and print the result  
print(Calc(int(input("Enter the number: "))))  
