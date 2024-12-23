import os

# Retrieve the target password from the environment variable
target_password = os.getenv("TARGET_PASSWORD")

try:
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        # Iterate through the dictionary and check each word
        found = False
        for line in file:
            word = line.strip()
            if word == target_password:
                print(f"Password found: {word}")
                found = True
                break
        
        if not found:
            print("Target password not found in dictionary.")
        
        # Prompt user for input to search in the dictionary
        user_password = input("Enter the password to search: ").strip()
        file.seek(0)  # Reset file pointer to the beginning
        found = False
        for line in file:
            word = line.strip()
            if word == user_password:
                print(f"Password found: {word}")
                found = True
                break
        
        if not found:
            print("User password not found in dictionary.")

except FileNotFoundError:
    print("Error: 'dictionary.txt' file not found. Please ensure the file exists in the current directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
