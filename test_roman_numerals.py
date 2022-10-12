def sortBinary(num):
    return format(num, 'b').count('1')

def sortByBinary(numbers):
    return sorted(numbers, key=lambda x: (sortBinary(x), x))

def sortRoman(num):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50}
    result = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or roman_numerals[c] >= roman_numerals[num[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result

def sortByRoman(numbers):
    return sorted(numbers, key=lambda x: (x.split()[0], sortRoman(x.split()[1])))

numbers = [2, 5, 32, 45, 55, 56, 57, 61]
print(sortByBinary(numbers))
names = ['barbara V', 'barbara III', 'matheus X', 'matheus III', 'zuma I']
print(sortByRoman(names))
