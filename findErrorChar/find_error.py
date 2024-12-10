import string
import os

# Define valid characters globally
valid_chars = set(string.ascii_letters + string.digits + '_-.')

def detect_invalid_lines_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return detect_invalid_lines(lines)

def detect_invalid_lines_from_folder(folderpath):
    filenames = os.listdir(folderpath)
    return detect_invalid_lines(filenames, folderpath)

def detect_invalid_lines(lines, folderpath=None):
    invalid_lines = []

    for line in lines:
        line = line.strip()  # Remove newline characters and surrounding spaces
        if any(char not in valid_chars for char in line):
            invalid_lines.append(line)
    
    # If from folder, include full paths for renaming
    if folderpath:
        invalid_lines = [(line, os.path.join(folderpath, line)) for line in invalid_lines]
    
    return invalid_lines

def rename_invalid_files(invalid_files, replacement_char):
    for filename, full_path in invalid_files:
        # Generate the new name by replacing invalid characters
        new_filename = ''.join(char if char in valid_chars else replacement_char for char in filename)
        new_path = os.path.join(os.path.dirname(full_path), new_filename)
        os.rename(full_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Main logic
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
        print("\nFiles with invalid characters:")
        for invalid_file in invalid_lines:
            if isinstance(invalid_file, tuple):  # For folder filenames, print just the name
                print(invalid_file[0])
            else:
                print(invalid_file)
        
        # Offer to rename files
        if choice == "2":  # Renaming is only applicable for folder files
            rename_choice = input("\nDo you want to rename invalid files? (y/n): ").strip().lower()
            if rename_choice == 'y':
                replacement_char = input("Enter the replacement character (_ or -): ").strip()
                if replacement_char not in ('_', '-'):
                    print("Invalid replacement character. Only '_' and '-' are allowed.")
                else:
                    rename_invalid_files(invalid_lines, replacement_char)
            else:
                print("No files were renamed.")
    else:
        print("\nNo invalid lines or filenames detected.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

input("\nPress Enter to exit...")