def factorial(n):
    if n > 1:
        fact = 1
        for i in range(1,n+1):
            fact *= i   
    else:
        fact = 1
    return f"Factorial of {n} is : {fact}"
print(factorial(int(input("Enter the number: "))))
