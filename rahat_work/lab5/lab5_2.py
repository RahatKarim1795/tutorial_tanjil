import random

def read_spells(filename: str) -> list[str]:

    spells = []
    spell_file = open("spells.txt", "r", encoding = "utf-8")

    spells = spell_file.readlines()
    spell_file.close()

    return (spells)


def get_random_spell(spells: list[str]) -> str:

    range = int(len(spells)) - 1
    rand_position = random.randint(0, range)
    spell = spells[rand_position]
    spell = spell.replace('\n','')

    lowercase_spell = ""

    for i in spell:
        if ord(i)>=65 and ord(i)<=90:
            current_ascii = ord(i)
            new_ascii = current_ascii + 32
            new_char = chr(new_ascii)
            lowercase_spell = lowercase_spell + new_char
        else:
            lowercase_spell = lowercase_spell + i

    return(lowercase_spell)


def display_header():
    for i in range(60):
        print("#",end ="")
        
    print('\nHarry Potter Keyboard Trainer')
    for i in range(60):
        print("#",end ="")

    print("\n")



def display_instructions():
    instruction = open("F:\\tutorial_tanjil\\university resources\\instructions.txt", "r", encoding = "utf-8")
    print(instruction.read())


def get_user_input(spell: str) -> str:

    typed_spell = input("Type the following spell: " + spell + "\n")

    return(typed_spell)
    

def display_feedback(spell: str, user_input: str):

    lowercase_typed_spell = ""

    for i in user_input:
        if ord(i)>=65 and ord(i)<=90:
            current_ascii = ord(i)
            new_ascii = current_ascii + 32
            new_char = chr(new_ascii)
            lowercase_typed_spell = lowercase_typed_spell + new_char
        else:
            lowercase_typed_spell = lowercase_typed_spell + i

    if lowercase_typed_spell == spell:
        print("Correct!")
    else:
        print("Incorrect!\nThe spell was: " + spell)

def main() -> None:
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)
main()
