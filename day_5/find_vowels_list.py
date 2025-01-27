def check_vowels(message):
    '''
    Function to identify the vowels present in the user input and count their occurrences using list.
    Args:
        message (str): user input for checking the vowels.
    Output:
        Displays the vowels present and the number of times they're repeated.
        If no vowels are found, it will notify the user.
    
    Example:
            Enter a message to check the number of vowels: HELLO FRIEND
            Please find below the vowels present in your message:
            Vowel   Total number
            e        2
            i        1
            o        1
    '''
    # Check if the input message is empty
    if not message:
        print("No message entered.")
        return
    
    # Define vowels with their initial count set to 0
    vowels = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]
    
    # Loop through each character in the message
    for char in message:
        if char.isalpha():  # Only count alphabetic characters
            for vowel in vowels:
                # Check if the character matches the vowel (case insensitive)
                if char.lower() == vowel[0]:
                    vowel[1] += 1
    
    # Output the results
    print("Please find below the vowels present in your message:")
    print("Vowel\tTotal number")
    
    # Check if any vowel count is greater than 0, otherwise notify no vowels found
    found_vowels = False
    for vowel in vowels:
        if vowel[1]:
            found_vowels = True
            print(f"{vowel[0]}\t{vowel[1]}")
    
    if not found_vowels:
        print("No vowels found in the message.")

# Taking input from the user
message = input("Enter a message to check the number of vowels: ")
check_vowels(message)