# Task 1  
- Create a dictionary with student names as keys and their marks as values  
student_dict = {"alice": 85, "rajesh": 90, "ram": 100}

- Take student name as input from the user  
Enter_name = input("Enter the Student's name: ")

- Convert the entered name to lowercase and check if it exists in the dictionary  
if Enter_name.lower() in student_dict:  
   - If found, print the marks of that student  
    print(f"{Enter_name}'s marks: {student_dict[Enter_name.lower()]}")  
else:  
    - If not found, display a message  
    print("Student not found.")


# Task 2  
- Create a list of numbers from 1 to 10  
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

- Initialize an empty list to store extracted elements  
list_2 = []

- Loop through the first half of list_1 (i.e., first 5 elements)  
for i in range(len(list_1) // 2):  
    list_2.append(list_1[i])  - Append each element to list_2  

- Print the extracted first five elements  
print(f"Extracted first five elements: {list_2}")

- Print the reversed version of the extracted elements  
print(f"Reversed extracted elements: {list_2[::-1]}")  
