import random
import time

def make_roll() -> tuple:

    rolled_numbers = []

    # check to see if user ready
    x = input("Ready to roll? (y/n) : ")

    if x.lower() == 'y':
        for i in range(5):
            random_roll = random.randint(1, 6)
            rolled_numbers.append(random_roll)

    elif x.lower() == "exit":
        quit()

    else:
        make_roll()
    
    return rolled_numbers
    
    

def sum_of_given_number(roll, number) -> int:
    """
    Returns the sum of the values in the roll that match the given number.

    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    # roll = (2,6,2,6,1)
    # number = 6
    """

    total = 0

    for i in roll:
        if i == number:
            total += number
    
    return total


def fill_upper_section(roll) -> list:
    """
    Returns a list of the sums of all values in the roll.
    roll = (2, 1, 5, 1, 5)
    """

    # upper_section = [0 position, 1 position, 2 position.....]
    # upper_section = [sum of 1, sum of 2, sum of 3, ..., sum of 6]
    upper_section = []

    for i in range(1,7):

        sum_of_current_number = sum_of_given_number(roll, i)

        upper_section.append(sum_of_current_number)
        
    return upper_section
    

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']

    # upper_section_scores = [2,0,0,8,0,12] example upper section score coming from main()

    for position in range(0,6):
        
        # position starts from 0 and ends at 6

        category = names[position] # save value from "names" list

        score = upper_section_scores[position] # save value (in same position) from "upper_section_scores" list

        print(category + ": " + str(score))
    


def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    count = 0
    sum = 0

    for i in range(1,7):
        for j in roll:
            if i == j:
                count+=1
        if count == number:
            for num in roll:
                sum += num
            break
        count = 0

        
    
    return sum


def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    num = roll[0]
    isYahtzee = True
    for i in roll:
        if i != num:
            isYahtzee = False
    
    if isYahtzee == True:
        return 50
    else:
        return 0

def print_c(roll):

    print("Rolling the dice", end="", flush=True)

    for _ in range(2):
        time.sleep(1)
        print(".", end="", flush=True)
        
    
    time.sleep(1)
    print(" (", end="", flush=True)
    for i in roll:
        print(i, end=",")

    print(")")



def main():
    """
    Main function.
    """
    # Version 1 code
    # TODO: Calculate and display "3 of a kind" for the given roll
    # TODO: Calculate and display "4 of a kind" for the given roll
    # TODO: Calculate and display "Yahtzee" for the given roll

    random_roll = make_roll()
    print_c(random_roll)

    x = input("roll again? (y/n): ")
    while x != 'n':
        random_roll = make_roll()
        print_c(random_roll)
        x = input("roll again? (y/n): ")

    

    upper_section_scores = fill_upper_section(random_roll)
    # print(upper_section_scores)
    display_upper_section(upper_section_scores)
    print("Three of a kind: " + str(num_of_a_kind(random_roll,3)))
    print("Four of a kind: " + str(num_of_a_kind(random_roll,4)))
    print("Yahtzee: " + str(yahtzee(random_roll)))

    # roll3 = [3,3,1,2,3]
    # roll4 = [1,1,1,2,1]
    # rollY = [4,4,4,3,4]

    # print(num_of_a_kind(roll3, 3))
    # print(num_of_a_kind(roll4, 4))
    # print(yahtzee(rollY))




if __name__ == "__main__":
    main()
