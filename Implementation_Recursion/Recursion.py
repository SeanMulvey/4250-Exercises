# Implemntation for recursion exercise
# Sean Mulvey
###################################################################################
# Problem:
    # Using Recursion; take two numbers in from the user (a human) and add them 
    # together then separate the least significant digit and add it the remaining 
    # digits and so on until you have a single digit answer. 
    # EX: 87345 => 8734+5= 8739 => 873+9 = 882 => 88 + 2 = 90 => 9+0 =9
###################################################################################
# Constraints:
    # Must use recursion

    # Must take input from a human user
###################################################################################
# Implied Constraints:
    # User input must be 2 whole numbers (integers) as that is the only way to
    # guarantee a single digit result
###################################################################################
# Things to keep in mind:
    # Input validation
        # Handle error checking on input so we can guarantee the input was 2 integers
###################################################################################
# Solution steps:
    # 1. Get input from user
    # 2. Validate input from user, if invalid reprompt
    # 3. Sum input to get total
    # 4. Pass total through recursive method
    # 5. Check if integer is negative
    # 6. If positive, check if integer % 10 = integer, if so exit since it is reduced to one digit
    # 7. If negative, check if absolute value of integer % 10 = absolute value of integer, if so exit since its reduced to one digit (aside from negative sign)
    # 6. Get LSD by using % 10
    # 7. Remove LSD from integer
    # 8. If integer is positive add LSD to integer, else subtract
    # 9. Return recursive method with new integer
    # 10. ???
    # 11. Get an A in this class
    # 12. Get a job
    # 13. Get a gazillion dollars
    # 14. Take over world
    # 15. Learn how to juggle
###################################################################################


def Main():
    # gets the sum of inputs from the user
    num = GetInput()
    ReduceInt(num)


# This method gets the input from the user and verifies it is an integer
def GetInput():
    # The sum to be returned for the recursive method
    total = 0
    # Used to determine the amount of integers we want the user to input
    inputCount = 2
    i = 0
    # Used a while loop here to sum the input so it would be easier to not iterate on failed input attempts
    while i < inputCount:
        try:
            temp = int(input("Enter an integer: "))
            total += temp
            i += 1
        except ValueError:
            print("ERROR: Input must be a valid integer! Try again!")
    return total

# This is the recursive method that adds the LSD to the integer until there is a single digit remaining
def ReduceInt(num):
    print(num)
    # Need to check if num is negative because the result will always be atleast 2 digits (negative sign)
    if num >= 0:
        # Exit condition of the number being only one digit
        if num == num % 10:
            return
    # Check to see if the absolute value is one digit
    elif abs(num) == abs(num) % 10:
        return

        
    print("=>")
    # Get Least Significant Digit
    lsd = num % 10
    print(f"{num // 10} + {lsd}")
    # Remove Least Significant Digit
    num = num // 10
    if num < 0:
        num -= lsd
    else:
        # Add LSD to new num
        num += lsd
    

    # Iterate
    return ReduceInt(num)
    
    


# Starter
Main()