def remove_duplicates(sorted_array):
    # Initialize an empty list to store unique elements
    unique_elements = []

    # Iterate through the sorted array
    for num in sorted_array:
        # If the current element is not already in the unique elements list, add it
        if num not in unique_elements:
            unique_elements.append(num)

    return unique_elements


# Sample Input
input_array = [15, 14, 25, 14, 32, 14, 31]

# Sorting the input array (if not already sorted)
input_array.sort()

# Remove duplicates from the sorted array
result = remove_duplicates(input_array)

# Print the sorted array with duplicates removed
print("Sample Input: Array =", input_array)
print("Sample Output: Sorted Array =", result)