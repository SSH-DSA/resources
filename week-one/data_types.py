# Python is known as a dynamically typed language,
# which means that we don't have to declare the type of a variable when we create one.
# Python automatically assigns the data type to the variable according to the value it holds.

# In languages like C we have to implicitly declare the data type of a variable.

# # Example:
# number = 3 # integers (whole numbers)
# # str_num = '3'
# # string = "Hello, World!"
# float_number = 4.5
# # truth = True
# # lie = False
# # none = None
# # # type()    
# # print(type(none))

# # number = str(int(input("Enter a number:")))

# # print(type(number))


# # print(type(str(float_number)))








# # The variables number, string, and float_number are of type int, str, and float respectively.

# # # We can check the type of a variable using the type() function. 
# # # EXERCISE 2 mins
# # # Use the type() function to check the data type of the variables number, string, and float_number.

# # #OPERATIONS ON NUMBERS (INT AND FLOATS)
# # # Python supports the following operations on numbers:
# # # Addition (+)
# # print(3 + 5)
# # # # Subtraction (-)
# # print(3 - 5)
# # # # Multiplication (*)
# # print(3 * 5)
# # # Division (/)

# print("The result of the division is: ", type(8 / 3))
# # # Floor Division (//)
# print("The result of the floor division is: ",type(8 // 3 ))


# # # Modulus (%)
# print("The remainder of the division is: ", (3 % 3))
# # # Exponentiation (**)
# print(3 ** 2)

# #EXERCISE 5 mins
# # Use the operations above to perform the following calculations:
# """
#    Create two variables a and b and assign them values of your choice
#     Add a and b
#     Subtract b from a
#     Multiply a and b
#     Divide a by b
#     Find the remainder when a is divided by b
#     Find a raised to the power of b
#     Find the floor division of a by b 
#     Print the type of the result of each operation
# """


# # OPERATIONS ON STRINGS
# # Strings are immutable, which means that once they are created, they cannot be changed.
# # However, we can perform operations on strings to create new strings.
# # The following operations are supported on strings:

# # Different types of strings
# # Single quotes (' ')
# # Double quotes (" ")
# # Triple quotes (''' ''')
# # Triple quotes (""" """)
# # Example:
# print("Mira\s, World!")
# print("Hello, 
      
#       World!")
# print('''Hello, 
      
#       World!''')
# print("""Hello,
# lorem ipsum dolor sit amet, 'consectetur adipiscing elit. Nulla nec odio eget urna aliquet tincidunt
# World!""")
# cheese = "cheddar"
# cheese = cheese +  " cheese"
# cheese = cheese * 3

# print(cheese)
# # Concatenation (+)
# # The + operator is used to concatenate two strings.
# # Example:
# print("Hello" + "World")
# # Repetition (*)
# # The * operator is used to repeat a string a given number of times.
# # Example:
# print("Hello" * 3)

# # Indexing
# # We can access individual characters of a string using indexing.
# # Indexing starts from 0.
# # Example:
string = "Hello,World!"
# string[3] = "h"
# print(string[::-1])
# # Slicing
# # We can access a substring of a string using slicing.
# # Example:
# string = "Hello, World!"
# print(string[0:5])
# # The above code will print "Hello".
# # The syntax for slicing is string[start:end].
# # The start index is inclusive, and the end index is exclusive.
# # If the start index is not given, it is assumed to be 0.
# # If the end index is not given, it is assumed to be the length of the string.
# # Example:
# string = "Hello, World!"

# print(string[:5])
# print(string[7:])
# # The above code will print "Hello" and "World!" respectively.
# # The start and end indices can also be negative.
# # Example:
# string = "Hello, World!"
# print(string[-6:-1])
# # The above code will print "World".
# # The negative indices are counted from the end of the string.
# # The index -1 refers to the last character of the string.
# # The index -2 refers to the second last character of the string, and so on.
# # The index -0 refers to the first character of the string, so it is the same as 0.
# # The index -len(string) refers to the first character of the string, so it is the same as 0.
# # The index -len(string) - 1 refers to the last character of the string, so it is the same as -1.

# #EXERCISE 5 mins
# # Take in a string from the user and print the first 3 characters of the string
# # Take in a string from the user and print the last 3 characters of the string
# # Take in a string from the user and print the middle 3 characters of the string

# # The len() function
# # The len() function is used to find the length of a string.
# # Example:
# string = "Hello, World!"
# print(len(string))
# # The above code will print 13.

# # The in operator
# # The in operator is used to check if a substring is present in a string.
# # Example:
# string = "Hello, World!"
# print("Hello" in string)
# # The above code will print True.

# # The not in operator
# # The not in operator is used to check if a substring is not present in a string.
# # Example:
# string = "Hello, World!"
# print("Hello" not in string)
# # The above code will print False.

# #lower and upper
# #The lower() method returns the string in lower case.
# #The upper() method returns the string in upper case.
# # The lower() and upper() methods do not modify the original string, but return a new string.
# # the title() method returns the string in title case.
# # Example:
string = " HelLo, woRld!"
new_string = string.strip()
no_space = string.replace(" ", "")
# print(new_string)
print(no_space)
# print(string)

# #Example:
# string = "Hello, World!"
# print(string.lower())
# print(string.upper())

# # writing a program that checks if a string is a palindrome
# # A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
# # Example: madam, racecar, 12321


