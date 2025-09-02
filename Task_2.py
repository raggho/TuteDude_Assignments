def write_and_append_file(filename):
    try:
        user_input = input("Enter text to write into the file: ")
        with open(filename, "w") as file:
            file.write(user_input + "\n")
            
        more_input = input("Enter additional text to append: ")
        with open(filename, "a") as file:
            file.write(more_input + "\n")
            
        print("\nFinal content of the file:")
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    write_and_append_file("output.txt")
