import string
import os

def detect_invalid_lines_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return detect_invalid_lines(lines)

def detect_invalid_lines_from_folder(folderpath):
    filenames = os.listdir(folderpath)
    return detect_invalid_lines(filenames)

def detect_invalid_lines(lines):
    valid_chars = set(string.ascii_letters + string.digits + '_-.')  # Allowed characters
    invalid_lines = []

    for line in lines:
        line = line.strip()  # Remove newline characters and surrounding spaces
        if any(char not in valid_chars for char in line):
            invalid_lines.append(line)

    return invalid_lines

print("Choose an option:")
print("1. Read filenames from a text file")
print("2. Read filenames from a folder")
choice = input("Enter your choice (1 or 2): ").strip()

try:
    if choice == "1":
        input_file = input("Enter the path to the text file: ").strip()
        invalid_lines = detect_invalid_lines_from_file(input_file)
    elif choice == "2":
        folder_path = input("Enter the path to the folder: ").strip()
        invalid_lines = detect_invalid_lines_from_folder(folder_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        exit()
    if invalid_lines:
        print("\nLines with invalid characters or spaces:")
        for invalid_line in invalid_lines:
            print(invalid_line)
    else:
        print("\nNo invalid lines detected.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
