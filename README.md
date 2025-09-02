def write_and_append_file(filename):
    try:
        # Step 1: Take user input and write it to the file (overwrite if exists)
        user_input = input("Enter text to write into the file: ")
        with open(filename, "w") as file:  # "w" mode = write
            file.write(user_input + "\n")

        # Step 2: Take additional input and append it to the same file
        more_input = input("Enter additional text to append: ")
        with open(filename, "a") as file:  # "a" mode = append
            file.write(more_input + "\n")

        # Step 3: Read and display the final content of the file
        print("\nFinal content of the file:")
        with open(filename, "r") as file:  # "r" mode = read
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    write_and_append_file("output.txt")


def write_and_append_multiple(filename):
    try:
        # Step 1: First input overwrites/creates the file
        user_input = input("Enter text to write into the file: ")
        with open(filename, "w") as file:  # "w" mode = write
            file.write(user_input + "\n")

        # Step 2: Keep asking for more input until user types 'exit'
        while True:
            more_input = input("Enter text to append (or type 'exit' to stop): ")
            if more_input.lower() == "exit":
                break
            with open(filename, "a") as file:  # "a" mode = append
                file.write(more_input + "\n")

        # Step 3: Read and display the final content of the file
        print("\nFinal content of the file:")
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    write_and_append_multiple("output.txt")
