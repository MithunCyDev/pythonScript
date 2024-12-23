import itertools
import string
import time

def generate_combinations(characters, max_length, target_password):
    """
    Generate prioritized combinations of the given characters up to max_length.
    """
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            combination_str = ''.join(combination)
            print(f"Trying combination: {combination_str}")  # Display each combination
            if combination_str == target_password:
                return combination_str
    return None

def find_password(input_password, max_length=5):
    """
    Try to find the input password using prioritized brute-force combinations.
    """
    # Prioritize lowercase letters first, then expand to full set
    prioritized_sets = [
        string.ascii_lowercase,              # Step 1: Lowercase letters
        string.ascii_lowercase + string.digits,  # Step 2: Lowercase + digits
        string.ascii_letters + string.digits,    # Step 3: Lower + Upper + digits
        string.ascii_letters + string.digits + "!@#$%^&*()",  # Step 4: Full set
    ]
    
    print("Starting optimized password brute-force...")
    start_time = time.time()
    
    for char_set in prioritized_sets:
        print(f"Using character set: {char_set}")
        result = generate_combinations(char_set, max_length, input_password)
        if result:
            end_time = time.time()
            print(f"\nPassword found: {result}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            return
    
    print("\nPassword not found. Try increasing the max_length.")

# User input for the password
user_password = input("Enter your password: ").strip()

# Start brute-force with max length 5 (you can increase this, but it will take longer)
find_password(user_password, max_length=5)
