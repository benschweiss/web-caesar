import string
import math

def alphabet_position(letter):
    result = ''
    alpha = string.ascii_lowercase
    alpha_up = string.ascii_uppercase
    if letter.isupper() == True:
        result = alpha_up.find(letter.upper())
    elif letter.islower() == True:
        result = alpha.find(letter.lower())

    return(result)


def rotate_character(char,rot):
    if type(char) is int:
        result = char + rot
    elif char.isalpha() == True:
        result = ''
        char_pos = alphabet_position(char)
        new_char_pos = char_pos + int(rot)
        alpha = string.ascii_lowercase
        alpha_up = string.ascii_uppercase
        if new_char_pos<26:
            if char.isupper() == True:
                char = str(char)
                result = result + alpha_up[new_char_pos]
            elif char.islower() == True:
                char =str(char)
                result = result + alpha[new_char_pos]
        if new_char_pos>=26:
            if char.isupper() == True:
                char = str(char)
                result = result + alpha_up[new_char_pos%26]
            elif char.islower() == True:
                char =str(char)
                result = result + alpha[new_char_pos%26]
    else:
        result = char

    return(str(result))



def encrypt(text,rot):
    result = ''
    for i in text:
        result = result + rotate_character(i,rot)

    return(result)
