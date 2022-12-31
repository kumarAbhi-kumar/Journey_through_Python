"""
The simplest thing we require from a programming language is:
1. it should take some input and
2. give some output
"""

name = input("Enter your name: ")
print("Hello World!")
print("This is", name)

'''Above written code highlights 2 python built-in functions:
1. input(): This is used to receive input from the user.
            Few things to note:
            1. We can prompt a message to help the user better understand what is requirement.
            2. Do remember that no matter what you give as input its always a String.
                Even if a number is typed its received as a String...
                If you understand whats the difference between String and numeric data type, Its good.
                Else follow along... for further sessions...

2. print(): This is used to print the strings quoted inside the parenthesis() as output.
            Few basic things to note:
            1. Statement quoted under single quoted('') or ("") are general text and printed as it is.
            2. text written without quotes are considered variables and their values are printed.

There are many different ways to use print() in regards to general text and variables 
will cover them all in following sessions.'''