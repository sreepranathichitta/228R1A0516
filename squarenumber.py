# Function to print squares of numbers in a given range
def print_squares(start, end):
    for number in range(start, end + 1):
        print(f"The square of {number} is {number ** 2}")

# Example usage
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print_squares(start_range, end_range)