import random
import string
import time

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
    
def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    length = len(spell)
    ttt = round(int(length) * 0.3, 2)
    return ttt

def calculate_points(spell: str, user_input: str, user_time: float, player_score: int) -> int:
    target_time1 = get_target_time(spell)
    target_time2 = target_time1 * 1.5
    target_time3 = target_time1 * 2

    if user_input == spell:

        if user_time<=target_time1:
            print("Correct! Extraordinary timing!")
            update_score = 10
            player_score += 10

        elif user_time<=target_time2 and user_time>target_time1:
            print("Correct! Great timing")
            update_score = 6
            player_score +=6

        elif user_time<=target_time3 and user_time>target_time2:
            print("Correct! Good timing")
            update_score = 3
            player_score += 3

        elif user_time>target_time3:
            print("Correct!!")
            update_score = 1
            player_score += 1

    else:
        print("Incorrect!\nThe spell was: " + spell)
        update_score = -5
        player_score -= 5

    return update_score, player_score


def high_score():
    file = open("high_score.txt", "r")
    score = file.readline()
    file.close()
    return score



def save_high_score():
    file = open("high_score.txt", "w")
    file.write(score)
    file.close()
        

def main() -> None:
    score = 0
    spells = read_spells('spells.txt')
    
    display_header()
    
    game_on = True


    total = 0

    while game_on == True:
        spell = get_random_spell(spells)
        user_typed_input, user_typed_time = get_user_input(spell)

        
        current_score, total = calculate_points(spell,user_typed_input,user_typed_time, total)
        print(f"You get {current_score} points! Your score is: {total}")
        game_on = play_again()

    highest_score = high_score()
    if total > high_score():
        print("You have set a new high score.")

    else:
        print("The last highest score was:", score)
        
    print("Your final score is: " + str(score))

    
 
main()

