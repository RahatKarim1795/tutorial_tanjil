import random
import string

def read_spells(filename: str) -> list[str]:
    spells = []
    spell_file = open("spells.txt", "r", encoding="utf-8")
    spells = spell_file.readlines()
    return spells

def get_random_spell(spells: list[str]) -> str:
    spell_range = int(len(spells))
    rand_position = random.randint(1, spell_range)
    spell = spells[rand_position]
    spell = spell.replace('\n', '')

    lowercase_spell = ''
    for i in spell:
        if ord(i) >= 65 and ord(i) <= 90:
            ascii_number = ord(i)
            lowercase_ascii = ascii_number + 32
            lower_char = chr(lowercase_ascii)
            lowercase_spell += lower_char
        else:
            lowercase_spell += i



    return lowercase_spell

def display_header():
    for i in range(60):
        print('#', end="")
    print("\nHarry Potter Typing Trainer")
    for i in range(60):
        print('#', end="")
    print("")

    display_instructions()



def display_instructions():
    instruct_t = []
    instruct_file = open("instructions.txt", "r", encoding="utf-8")
    #instructions = instruct_file.readlines
    t_file = instruct_file.readlines()
    for line in t_file:
        instruct_t.append(line.strip())
    instruct_file.close()
    
    for i in instruct_t:
        print(i)






def get_user_input(spell: str) -> str:
    #print(display_instructions())
    user_input = input("Type the following spell: " + str(spell)+ "\n")
    return user_input



def display_feedback(spell: str, user_input: str):
        if user_input == spell:
            print("Correct")
        else:
            print("Incorrect")
            print("The spell was: " + str(spell))
            



def main() -> None:

    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)

main()


 