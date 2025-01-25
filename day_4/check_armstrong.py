def check_armstrong(number):
    '''
    This function checks whether the number is an Armstrong number or not.
    
    Args: 
        number (int): The number to be checked.

    Returns:
        bool: True if the number is an Armstrong number, otherwise False.

    Definition: An Armstrong number (also known as a Narcissistic number) of n digits is a number such that 
    the sum of its digits raised to the power of n is equal to the number itself.

    Example:
        Input: 153
        Computation: 1**3 + 5**3 + 3**3 = 153
        Result: 153 is an Armstrong number.
    '''
    if number<0:
        return False
    number_str=str(number)
    len_number = len(number_str)
    # Using list comprehension to calculate the sum of digits raised to the power of len_number
    processed_number = sum(int(digit) ** len_number for digit in number_str)
    # Return boolean value after evaluating whether number matches the processed_number
    return number==processed_number

number=int(input("Please enter a number:"))
print(f"{number} is {'an Armstrong' if check_armstrong(number) else 'not an Armstrong'} number")