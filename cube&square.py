def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

try:
    user_number = float(input("Enter a number: "))
    square_result, cube_result = calculate_square_and_cube(user_number)
    print("Square of", user_number, "is:", square_result)
    print("Cube of", user_number, "is:", cube_result)
except ValueError:
    print("Please enter a valid number.")
