'''
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(str):
    count = 0
    letters = []
    for c in str:
        if c not in letters:
            ms = "co{}e".format(c)
            if ms in str: count += str.count(ms)
            letters.append(c)
    return count

print(count_code('codexxcode'))