def sum_of_digits(num):
    total_sum = 0
    for digit in str(num):
        total_sum += int(digit)
    return total_sum

# Get user input for N value and the N-digit number
N = int(input("Enter N value: "))
input_number = int(input(f"Enter {N} digit number: "))

# Calculate the sum of digits
while input_number >= 10:
    input_number = sum_of_digits(input_number)

# Output the result
print(f"Sum of {N} digit number: {input_number}")