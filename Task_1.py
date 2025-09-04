student_dict = {"alice":85, "rajesh":90, "ram":100}

Enter_name = input("Enter the Student's name: ")

if Enter_name.lower() in student_dict:
    print(f"{Enter_name}'s marks: {student_dict[Enter_name.lower()]}")
else:
    print(f"Student not found.")
