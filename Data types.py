"""
Data types:
Data: It's the piece of information that is received by the computer.
Systems to act efficiently differentiates data among few basic categories:
"""

variable1 = 21
'''1. Integers: int -> (as used in Python)
            >> This defines the integers (numbers without decimal points).'''
print(type(variable1))
# By Using '#' we can write comments in program...
# We use type() function to print the data type of the variables.

variable2 = 21.21
'''2. Real: float
            >> This defines the numbers with decimal points.'''
print(type(variable2))

variable3 = 'K'
variable4 = 'hello'
variable5 = "How are you"
variable6 = "7"
'''3. String: str
            >> This defines a length of character withing single_quotes('') or double_quotes("")
            >> Even a number when enclosed within quotes are referred as strings.'''
print(type(variable3), type(variable4), type(variable5), type(variable6))

variable7 = True
variable8 = False
'''4. Boolean: bool
            >> These are boolean type values which indicates true or false only. 
            >> True and False must be written with their first initials capital.
            >> Various conditional statements gives their output as boolean values.'''

'''
These are the few built in data types commonly used in python.
We can also create our own data type in python called "Composite data type"...
We will look to them later.
'''