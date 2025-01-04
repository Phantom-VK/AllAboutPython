#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    swapped_string = ""
    for char in s:
        if char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char.upper()
    return swapped_string