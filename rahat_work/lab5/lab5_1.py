import string
import time
import random

def read_spells(filename: str) -> list[str]:

    spells = []
    spell_file = open("spells.txt", "r", encoding = "utf-8")

    spells = spell_file.readlines()
    spell_file.close()

    return (spells)


def get_random_spell(spells: list[str]) -> str:

    # i want an integer variable
    # i will store a random number between 1 and 184
    # i will use this number to call the spell at that position of the list
    # i will print the spell i got

    range = int(len(spells)) - 1

    rand_position = random.randint(0, range)

    spell = spells[rand_position]
    spell = spell.replace('\n','')

    # use loop to go through the string
    # find ascii code of each character
    # if ascii code is capital
    # change to lowercase using difference
    # otherwise no change

    lowercase_spell = ""

    for i in spell:
        # current_ascii = ord(i)
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):           #is the current character 'i' a capital letter?
            current_ascii = ord(i)            # find out ascii code of that character
            new_ascii = current_ascii + 32      # add the difference to find ascii of lowercase letter
            new_char = chr(new_ascii)         # use ascii to get the lowercase character
            lowercase_spell = lowercase_spell + new_char        #add the new character to the string
        else:
            lowercase_spell = lowercase_spell + i           #if the character is not capital letter, add the character to the string


    return(lowercase_spell)


def main():

    spells = read_spells('spells.txt')

    print('Harry Potter Keyboard Trainer')
       
    spell = get_random_spell(spells)
    print(spell)


main()