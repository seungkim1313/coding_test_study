"""
LeetCode Problem - EASY
258. Add Digits

Given an integer 'num', repeatedly add all its digits until the result has only one digit, and return it.

Example #1
input: num = 38
output: 2
Explanation:
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    return 2
"""

def add_digits(num):
    
    while len(str(num)) != 1:
        summation = 0
        for i in list(str(num)):
            summation += int(i)
        num = summation
    return num

print(add_digits(11))