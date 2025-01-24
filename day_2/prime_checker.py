def check_prime(number):
    '''
    Args:
        number (int): The integer to check for primality. Must be greater than or equal to 0.
    Returns:
        bool: True if the number is prime, False otherwise.
    Description:
        Checks whether the given integer is a prime number.
        A prime number is greater than 1 and has no divisors other than 1 and itself.

    Example:
        check_prime(2) -> True
        check_prime(4) -> False
        check_prime(17) -> True
    '''
    #Numbers less than or equal to 1 are not prime
    if(number <= 1 ):
        return False
    #2 is the only even prime number
    if(number == 2):
        return True
    # Exclude all even numbers greater than 2
    if(number %2 == 0):
        return False
    # Check for divisors from 3 to sqrt(number), skipping even numbers
    for i in range(3,int(number** 0.5) + 1, 2):
        if(number % i == 0):
            return False
    return True

#validating the input

while True:
    try:
        number = int(input("Enter a positive integer to check if it's prime: "))
        if number<0:
            print("Please enter a valid positive integer (natural number greater than or equal to 0).")
            continue
        is_prime=check_prime(number)
        break
    except ValueError:
        print("Please enter a valid positive integer (natural number greater than or equal to 0).")

#output
print(f"The number {number} is {'a prime' if is_prime else 'not a prime'} number.")

