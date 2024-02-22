from itertools import permutations


def unique_permutations(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)

    # Generate permutations of the digits
    perms = set(permutations(number_str))

    # Initialize a list to store unique permutations
    unique_perms = []

    # Iterate through each permutation
    for perm in perms:
        # Convert the permutation back to a number
        perm_num = int(''.join(perm))
        # Add the permutation to the list if it's not already present
        if perm_num not in unique_perms:
            unique_perms.append(perm_num)

    return unique_perms


# Sample Input
given_number = 143

# Get unique permutations of the given number
permutations = unique_permutations(given_number)

# Print the unique permutations
print("Permutations are:")
for perm in permutations:
    print(perm)