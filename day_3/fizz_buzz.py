def fizzbuzz(start=1, end=100):
    '''
    This program print 'start' to 'end' with the following rules:
    -For the multiples of 3, print "Fizz"
    -For the multiples of 5, print "Buzz"
    -For the multiples of 3 and 5, print "FizzBuzz"
    -For the other numbers, print the number itself.    

    Parameters:
    start (int): The starting number of the range. Default is 1.
    end (int): The ending number of the range. Default is 100.
    Example:
    fizzbuzz(1, 15)
    Output:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    '''

    for i in range(start, end + 1):
        # Check for multiples of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Check for multiples of 3
        elif i % 3 == 0:
            print("Fizz")
        # Check for multiples of 5
        elif i % 5 == 0:
            print("Buzz")
        # If none of the above conditions are met, print the number
        else:
            print(i)
# Call the function with the start and end range
fizzbuzz(1,100)