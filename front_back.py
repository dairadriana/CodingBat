'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(str):
    if len(str) <= 1:
        return str
    middle = str[1:-1]
    my_string = str[-1] + middle + str[0]
    return my_string
