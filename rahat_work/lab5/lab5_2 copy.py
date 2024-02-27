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
    a = 1
    # take the input from user and give it back to main() function
    # take the input as per the question (the writing)
    

def display_feedback(spell: str, user_input: str):
    a = 1
    # question does not have upper case or lowercase requirement
    # but for comparison better to have both same case letter/string
    # so, we want the input from the user and the spell chosen to be same case
    # SO we transform the input to same case as chosen random spell
    # after this, compare if the input is same as the random spell
    # if correct/incorrect show output as per the quest


def main() -> None:
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)
main()
