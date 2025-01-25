def check_armstrong(start,end):
    '''
        Function: This program find all the armstrong numbers within the range provided.
    Args:
        start(int): Starting value of the range
        end(int): Ending value of the range
    Output: List of armstrong numbers within the range from start to end.

    Definition: An Armstrong number (also known as a Narcissistic number) of n digits is a number such that 
    the sum of its digits raised to the power of n is equal to the number itself.

    Example: 
        Input: start=20, end=200
        List of armstrong numbers between 20 and 200: [153]

    '''
    armstrong_list=[]
    for check_num in range(start,end+1):
        number_str=str(check_num)
        len_digit=len(number_str)
        # Each digit of the number is raised to the power of the total number of digits (len_digit),
        processed_num=sum(int(digit)**len_digit for digit in number_str)
        if processed_num == check_num:
            armstrong_list.append(check_num)
    return armstrong_list

def get_input():
    '''
    This function gets the start and end range and validate the input.
    returns:
        int(start): Return the starting range for the armstrong number lookup 
        int(end): Returns the ending range for the armstrong number lookup 
    '''
    while True:
        try:
            start=int(input("Enter the start range: "))
            end=int(input("Enter the end range: "))
            if(end<0 or end<start or start<0):
                raise ValueError
            return start,end
        except ValueError:
                print("Invalid input! Conditions:\n\t1. Values must be positive integers.\n\t2. End range must be greater than the start range.")

start,end=get_input()
armstrong_list=check_armstrong(start,end)
print(f"List of armstrong numbers between {start} and {end}: {armstrong_list}")