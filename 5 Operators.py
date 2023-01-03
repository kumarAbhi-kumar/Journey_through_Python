"""
Operators: these are certain characters
    >> which are applied to mostly variables (here termed as operands)
    >> hence an operation takes place
    >> a + b, here a and b are variables which we term as operands and + is an "addition" operator,
        > acting on a & b and performing addition on the values of a & b.

There are different kind of operators in python.

We will be covering them when their application in understandable in actual sense of uses.
for example the use of relational operator is understandable when we understand Conditional statements.
So ya understand when needed.
"""

'''
Here we discuss 2 types of operators:
    1. Arithmetic Operator.
    2. Assignment operator.
'''

'''Arithmetical Operator: used to perform arithmetic tasks.
1. + : Addition
2. - : Subtraction
3. * : Multiplication
4. / : Division (returns quotient real/floating point values)
5. //: Integral Division (returns Integral quotient without decimal values.)
6. **: Exponent (Application: base**power -> 2**3 i.e 2 to the power 3. Output: 8)
7. % : Returns remainder on division'''

first_value = 45
second_value = 6

total = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
integral_quotient = first_value // second_value
exponent = first_value ** second_value
remainder = first_value % second_value

"""
Assignment Operator:
    >> 1. = : its one of simplest assignment operator.
        > It basically substitute the value on the RHS to variable on LHS.
    >> 2. There is a combination of Assignment and Arithmetic.
        > Often referred as Shorthand operator.
        > +=, -=, *=, /=.
        > These are used to perform the mathematical operation and assign it to same variable.
"""
a = 6
# Increasing a value by a particular value. Say by 1.
a += 1
print(a)
# Now the value of "a" is increased by 1. Similarly, we can subtract, multiply, divide & other such operations as well.
b = 7
b //= 7
print(b)
