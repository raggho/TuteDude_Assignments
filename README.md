# Task 1
# Ask the user to enter a number and convert the input string to an integer  
n = int(input("Enter a number: "))

# Check if the number is even using the modulo operator (%)  
if n % 2 == 0:
    # If the remainder when n is divided by 2 is 0, then it's even
    print(f"{n} is an even number")
else:
    # If the remainder is not 0, then it's odd
    print(f"{n} is an odd number")


# Task 2

# Initialize a variable 'sum' to 0. This will store the running total.
sum = 0

# Use a for loop to iterate over the numbers from 1 to 50 (inclusive)  
for i in range(1, 51):  # range(1, 51) generates numbers from 1 to 50
    sum += i            # Add the current number 'i' to the sum

# After the loop ends, print the total sum  
print(f"The sum of numbers from 1 to 50 is:", sum)
