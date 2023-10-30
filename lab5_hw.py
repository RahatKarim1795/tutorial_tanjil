import random
import time
import string

capital_letters = string.ascii_uppercase
lowercase = string.ascii_lowercase


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


# def get_user_input(spell: str) -> str:

#     typed_spell = input("Type the following spell: " + spell + "\n")

#     return(typed_spell)

def get_user_input(spell: str) -> (str, float):

    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")

    return user_input, user_time


def play_again() -> bool:
    h = input("Press 'Y' to play again\nPress 'N' to see score: ")

    if h == 'y' or h == 'Y':
        return True
    elif h == 'n' or h == 'N':
        return False
    
def get_target_time(spell: str) -> float:
    length = len(spell)
    ttt = int(length) * 0.3

    return ttt

def calculate_points(spell: str, user_input: str, user_time: float) -> int:

    target_time1 = get_target_time(spell)
    target_time2 = target_time1 * 1.5
    target_time3 = target_time1 * 2

    if user_input == spell:

        if user_time<=target_time1:
            print("Correct! Extraordinary timing!")
            update_score = 10

        elif user_time<=target_time2 and user_time>target_time1:
            print("Correct! Great timing")
            update_score = 6

        elif user_time<=target_time3 and user_time>target_time2:
            print("Correct! Good timing")
            update_score = 3

        elif user_time>target_time3:
            print("Correct!!")
            update_score = 1

    else:
        print("Incorrect!\nThe spell was: " + spell)
        update_score = -5

    return update_score

def find_highscore(total):
    # open high_score file
    file = open("high_score.txt", "r", encoding = "utf-8")
    all_high_scores = file.readlines() #store all data into a list
    file.close()

    high_scores1 = [] # we will store only the scores without name here
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #we want to remove all characters and only keep numbers

    for score_line in all_high_scores:
        score = score_line.strip(chars) # here the characters are being stripped

        score = score.strip(":") # here the ":" are being stripped

        high_scores1.append(score) # now we have only number, store it in a list

    for i in high_scores1:      #the users score is compared to every score
        if total > int(score):
            print(f"Congratulations! Your score of {total} is higher score of {score}")
            
            new_name = input("Enter your name to save your highscore: ") #if user has highscore ask for name

            f = open("high_score.txt", "a", encoding = "utf-8")
            f.write("\n" + new_name + ":" + str(total)) #add the name to the file
            f.close()

    see_score = input("see all high scores? (y/n): ") # user can see the highscore list
    
    if see_score == "y" or see_score== "Y":
        file = open("high_score.txt", "r", encoding = "utf-8")
        all_high_scores = file.readlines()
        
        print(all_high_scores)
        file.close()


def main() -> None:

    spells = read_spells('spells.txt')
    display_header()
    display_instructions()

    game_on = True

    total = 0

    while game_on == True:
        spell = get_random_spell(spells)
        user_typed_input, user_typed_time = get_user_input(spell)

        # score = display_feedback(spell, user_input)
        
        current_score = calculate_points(spell,user_typed_input,user_typed_time)
        total += current_score
        game_on = play_again()
    
    print ("\nYour total score is: " + str(total))

    find_highscore(total)

main()


