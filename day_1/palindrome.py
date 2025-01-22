def message_rev(string):
    '''
    Function to reverse a given string.

    Args: 
        string (str): The input string to be reversed.
    
    Returns: 
        str: The reversed string.
    '''
    reversed_string = string[::-1] # Reverse the string using slicing
    return reversed_string
# Taking input from the user 
message = input("Enter your message: ")
# Displaying the reversed message
print("Reversed message: ", message_rev(message))# Print the reversed string

