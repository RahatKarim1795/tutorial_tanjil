from yahtzee2 import num_of_a_kind, yahtzee

def test_three_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "3 of a kind".
    """
    roll = [1,1,1,2,3]
    assert num_of_a_kind(roll, 3) == 8



def test_three_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "3 of a kind".
    """
    roll = [1,2,5,6,4]
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "4 of a kind".
    """
    roll = [1,2,2,2,2]
    assert num_of_a_kind(roll, 4) == 9

def test_four_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "4 of a kind".
    """
    roll = [1,4,4,6,5]
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    """
    Tests yahtzee() with a roll that has a yahtzee.
    """
    roll = [5,5,5,5,5]
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    """
    Tests yahtzee() with a roll that has no yahtzee.
    """
    roll = [2,3,4,4,5]
    assert yahtzee(roll) == 0

def main():
    test_three_of_a_kind_found()
    test_three_of_a_kind_not_found()
    test_four_of_a_kind_found()
    test_four_of_a_kind_not_found()
    test_yahtzee_found()
    test_yahtzee_not_found()


main()