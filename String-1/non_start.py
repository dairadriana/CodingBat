'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
'''

def non_start(a, b):
    a = a.replace(a[0], "")
    b = b.replace(b[0],"")
    return a+b