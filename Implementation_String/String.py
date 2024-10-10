# Implementation for string exercise
# Sean Mulvey
###############################################################################
# Problem: 
    # Take in a string (from a user or a file), compute the total number of 
    # occurrences of each character in the ASCII set. Print out the top three 
    # characters (with the most occurrences). Print out how many characters 
    # in the ASCII set you didn’t detect. Then print out the string in reverse 
    # order.
##############################################################################################################################################################
# Constraints:
    # Be able to take a string from a user OR a file

    # Only count ASCII characters

    # Get the 3 most prevalent ASCII characters

    # Print how many ASCII characters not present 

    # Print string in reverse order
##############################################################################################################################################################
# Initial thoughts:
    # Because I want to be able to take input from a user or a file, I should
    # have a method for user input and a method for file input. With that however,
    # How do I go about picking which one to read from? Do I prompt the user to choose?
    # If thats the case, what happens in the event where the user is unable to input?
    # Should I just make it with the assumption they are able to choose in order to facilitate
    # both options in a single solution, or should I instead create two completely separate solutions?

    # In order to determine if a character is in the ASCII set I can use ord() to get the Unicode and if
    # it is <= 127, it is ASCII. Another way is I could hardcode a hashmap that contains the ASCII set. 
    # This would probably be better as to avoid a weird bug with Unicode values that might occur, but for 
    # the sake of my sanity it would be better to just check the Unicode value

    # To keep track of the number of occurrences of each ASCII character I can probably use a hashmap where
    # the key is the ASCII character and the value is the number of occurrences for that character

    # If I use a hashmap for the occurences of each ASCII character in the input, then I could retrieve the 
    # 3 most prevalent by just sorting the hash map and getting the top 3 results

    # Actually now that I think about it, it probably would be better to hardcode the hash map. If I do that
    # then it would be much easier to get a count of all of the ASCII characters not present in the input. I 
    # could go ahead and get that by counting the number of keys with a value of 0.

    # Printing the string in reverse order should be pretty easy. I think all I need to do for that is iterate
    # through the string and push each character to a stack and when I reach the end, just pop each element
    # in the stack into a new string until the stack is empty and then print the new string, unless you want me
    # to reverse the string in place without taking up anymore memory. If thats the case, I would need to take 
    # index i and move it to -i and vice versa until I get to the halfway point of the string.
##############################################################################################################################################################
# Conclusion for initial thoughts:
    # For the purposes of this assignment, I'll have both input options in a single solution and prompt the user to choose one.
    # I'll include a file to read from for if they choose that option

    # Because it'll help out with the checking of ASCII characters that didn't occur, I'll use a hardcoded hashmap containing possible ASCII
    # characters. Hypothetically, if I were to do it using ord(), I would probably need to have a list of all Unicode values used and once the 
    # input is read, iterate from 0-127 and check to see if they are in the list of read Unicode values, and if not, get that value's ASCII character
    # and add it to a list of unused ASCII characters, returning the characters and the total number that was not used.

    # I'm going to assume that the string reversal does not need to be in place since we discussed in class that memory isn't really an issue in the modern day.
##############################################################################################################################################################

# Create a method to read from a file

# Create a method to read from user input

# Create a method that counts the ASCII characters in the input

# Create a method that returns the top 3 ASCII characters

# Create a method that reverses and prints out the string

# I can probably combine some of these
# As I input the string characters into the stack, I can count each one and increment the values in the hashmap

def Main():
    # Creates a copy of the ASCII hash map
    choice = input("Read from user input (u) or from a file (f)?: ")
    reader = ""
    if choice == "u":
        reader = UserInput()
    elif choice == "f":
        reader = FileInput("Implementation_String/test_file.txt")
    else:
        print("ERROR: Pick a valid option!")
        Main()

    map = Map()
    
    
    ReverseString(map, reader)
    PrintMostUsed(map)
    totalAscii = GetAsciiTotal(map)
    print(f"Number of Ascii characters used: {totalAscii}")
    print(f"Number of ASCII characters not used: {PrintNotUsed(map)}")


# Prints the amount of characters not used
def PrintNotUsed(map):
    count = 0
    for i in map:
        if map[i] == 0:
            count += 1
    return count

# Gets total amount of ASCII characters used
def GetAsciiTotal(map):
    total = 0
    for i in map:
        total += map[i]
    return total

# Gets 3 most used characters
def PrintMostUsed(map):
    # The amount of results to grab from the top
    topNum = 3
    # sorts map in descending order by value
    sortedMap = sorted(map.items(), key=lambda x: x[1], reverse=True)

     # Print the top 3 characters or fewer if the map is small
    for i in range(min(3, len(sortedMap))): 
        key, value = sortedMap[i]
        print(f"Character: '{key}', Occurrences: {value}")


# Method containing ASCII map
def Map():
    # Used GPT to generate this. Honestly didn't know I could use chr(). I thought I had to type each one out
    ascii_dict = {chr(i): 0 for i in range(128)}

    return ascii_dict



# method for user given input
def UserInput():
    return input("Enter a string: ")


def FileInput(path):
    with open(path, 'r') as file:
        contents = file.read()
    return contents

# Counts occurrences of each ASCII character 
def CharCounter(map, curr):
    if curr in map:
        map[curr] += 1
        
        



# Reverses string and counts occurrences
def ReverseString(map, input):
    # Used to save reversed string
    newStr = ""
    # Used to reverse string
    stack = []

    # Iterates through string to add it to stack and count occurrences
    for i in range(len(input)):
        stack.append(input[i])
        CharCounter(map, input[i])

    while stack:
        newStr += stack.pop()
    
    print(f"Reversed string: {newStr}")


# Starter
Main()