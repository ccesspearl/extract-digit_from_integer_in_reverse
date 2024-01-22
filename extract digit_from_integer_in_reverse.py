# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# Pseudocode 

# Create a function that will reverse the given number 
def reverse_number(given_number): 

# Inside the function, convert the given number to string 
    convert_string = str(given_number)

# Inside the function, reverse the given number string 
    reverse_number = convert_string[::-1]

# Inside the function, create a loop to have spaces to each numbers 
    for i in reverse_number:
        print(i, end= " ")

# Input the given number 
number = 123456

# Print the results 