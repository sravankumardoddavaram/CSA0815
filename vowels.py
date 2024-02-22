def count_vowels(statement):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Initialize a counter for vowels
    vowel_count = 0

    # Convert the statement to lowercase to make case-insensitive comparison
    statement = statement.lower()

    # Iterate through each character in the statement
    for char in statement:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1

    return vowel_count


# Sample Input statements
test_cases = [
    "India is my country",
    "All are my brothers and sisters",
    "Why dry sky",
    "Shy Try Cry",
    "EDUCATION"
]

# Test the program for each input statement
for idx, statement in enumerate(test_cases):
    num_vowels = count_vowels(statement)
    print(f"Test case {idx + 1}: {statement}")
    print(f"Number of vowels = {num_vowels}")