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
    
#################
## using while loop
#################

# def num_of_a_kind(roll, number) -> int:

#     # roll = [1,1,2,1,3]
#     # number = 3

#     count = 0
#     sum = 0
#     check_num = 1

#     for i in roll:
#         sum+=i

#     while check_num < 7:
#         for i in roll:
#             if i == check_num:
#                 count += 1
        
#         if count == number:
#             return sum

#         else:
#             count = 0
#             check_num += 1
    
#     return 0


#################
## using for loop
###################

def num_of_a_kind(roll, number) -> int:
    count = 0
    sum = 0

    for i in roll:
        sum+=i

    for i in range(1,7):   
        for j in roll:
            if i == j:
                count += 1
        
        if count == number:
            return sum

        count = 0

    return 0


def yahtzee(roll: tuple) -> int:

    num = roll[0]

    for i in roll:
        if i != num:
            return 0

    return 50


def display_lower_section(roll):
    print("Three of a kind: " + str(num_of_a_kind(roll,3)))
    print("Four of a kind: " + str(num_of_a_kind(roll,4)))
    print("Yahtzee: " + str(yahtzee(roll)))



def main1():

    random_roll = make_roll()


    print("Rolling the dice... " + str(random_roll))

    upper_section_scores = fill_upper_section(random_roll)
 
    display_upper_section(upper_section_scores)
    display_lower_section(random_roll)
   

if __name__ == "__main__":
    main1()
