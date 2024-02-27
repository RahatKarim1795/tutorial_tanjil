import random

def make_roll() -> tuple:

    rolled_numbers = []

    x = input("Ready to roll? (y/n) : ")

    if x.lower() == 'y':
        for i in range(5):
            random_roll = random.randint(1, 6)
            rolled_numbers.append(random_roll)
    
    return rolled_numbers
    
    

def sum_of_given_number(roll, number) -> int:
    total = 0
    for i in roll:
        if i == number:
            total += number
    
    return total


def fill_upper_section(roll) -> list:

    upper_section = []

    for i in range(1,7):
        sum_of_current_number = sum_of_given_number(roll, i)
        upper_section.append(sum_of_current_number)
        
    return upper_section
    

def display_upper_section(upper_section_scores: list) -> None:

    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']

    for position in range(0,6):
        category = names[position]
        score = upper_section_scores[position]
        print(category + ": " + str(score))



def main():


    random_roll = make_roll()

    print("Rolling the dice... " + str(random_roll))

    upper_section_scores = fill_upper_section(random_roll)

    display_upper_section(upper_section_scores)

if __name__ == "__main__":
    main()