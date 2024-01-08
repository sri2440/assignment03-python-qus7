#1.	Use the map function to double each element in a list of integers.

# List of integers
numbers = [1, 2, 3, 4, 5]

# Using map to double each element
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the result
print(doubled_numbers)


# 2.	Apply the filter function to extract only the odd numbers from a list.

# List of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to extract odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the result
print(odd_numbers)

# 3.	Write a lambda function that squares its input. Test the lambda function with a list of numbers.
# Lambda function to square its input
square_function = lambda x: x**2

# Test the lambda function with a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using map to apply the lambda function to each element
squared_numbers = list(map(square_function, numbers))

# Print the result
print(squared_numbers)

# 4.	Implement a function that takes a list of integers and uses a lambda function to find the product of each element and its square.
def product_of_element_and_square(numbers):
    # Using a lambda function to calculate the product of each element and its square
    product_function = lambda x: x * (x**2)
    
    # Applying the lambda function to each element using map
    product_results = list(map(product_function, numbers))
    
    return product_results

# Test the function with a list of integers
numbers = [1, 2, 3, 4, 5]

# Get the product of each element and its square
result = product_of_element_and_square(numbers)

# Print the result
print(result)
