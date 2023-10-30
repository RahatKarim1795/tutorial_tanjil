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



def main():
    # """
    # Main function.
    # """
    # # TODO: Roll the dice (and print as in demo)
    # # TODO: Fill the upper section
    # # TODO: Display the upper section

    random_roll = make_roll()


    print("Rolling the dice... ( " , end="")

    # time.sleep(3)

    for i in random_roll:
        print(i, end=",")

    print(")")

    upper_section_scores = fill_upper_section(random_roll)
    print(upper_section_scores)
    display_upper_section(upper_section_scores)

if __name__ == "__main__":
    main()