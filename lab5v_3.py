import random
import string

def read_spells(filename: str) -> list[str]:
    spells = []
    spell_file = open("spells.txt", "r", encoding="utf-8")
    spells = spell_file.readlines()
    spell_file.close()
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


#bhul
def display_instructions():
    instruct_t = []
    instruct_file = open("instructions.txt", "r", encoding="utf-8")
    t_file = instruct_file.readlines()
    for line in t_file:
        instruct_t.append(line.strip())
    instruct_file.close()
    
    for i in instruct_t:
        print(i)


def get_user_input(spell: str) -> str:
    user_input = input("Type the following spell: " + str(spell)+ "\n")
    return user_input



def display_feedback(spell: str, user_input: str):
    
    if user_input == spell:
        print("Correct")
        return True

    else:
        print("Incorrect")
        print("The spell was: " + str(spell))
        return False


def play_again() -> bool:

    while True:
        play_again = input("Do you want to practice more? (y/n) ")
        if play_again == 'Y' or play_again == 'y':
            return True
        elif play_again == 'N' and play_again == 'n':
            return False
        break
            

# use diplay feedback to find out if user input is correct or not
# if correct go into calculate points
# then find out the TTT and store the value
# then find out each tier of typing speed
# use the tiers to give points and show relevant output

        

def main() -> None:
    score = 0
    spells = read_spells('spells.txt')
    
    display_header()
    
    game_cont = True
    # tot_score = 0

    while game_cont:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)

        # current_score = display_feedback(spell, user_input)
        # tot_score += current_score

        
        if display_feedback(spell, user_input):
            score += 10
            print("You got 10 points! Your score is: " + str(score))
        else:
            score -= 5
            print("You lose! Your score is: " + str(score))
            
        game_cont = play_again()

    print("Your final score is: " + str(score))
    
 
main()
