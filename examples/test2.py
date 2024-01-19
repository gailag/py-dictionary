# 1. Fill in the function ‘count_vowels’ that takes in a string as an argument and returns the count of vowels (a, e, i, o, u) in that string. 
#   (Count both uppercase and lowercase vowels) 
#   Params: a string 
#   Returns: The total count of uppercase and lowercase vowels 

def count_vowels(string):
    vowels = 0
    
    for letters in string:
        if letters in "aeiouAEIOU":
            num_vowels =+ 1
    return vowels
            

# 2. Fill in the function 'reverse_name' that takes a name, converts it to uppercase, checks the length of the name.
# If the length is greater than 7 concatenate the reserve name before the uppercase name 
# If the length is not greater than 7 it concatenate the uppercase name before the reverse 

def reverse_name(name):
    uppercase = name.upper()
    length = len(name)

    reverse = name[::-1]
    if length > 7:
        concat = reverse + uppercase
    else: 
        concat = reverse + uppercase

    return concat 
