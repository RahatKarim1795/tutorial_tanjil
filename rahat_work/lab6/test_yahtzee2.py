import time

from lab6_v2 import num_of_a_kind, yahtzee



def test_three_of_a_kind_found():
    roll = [1,1,1,3,4]
    assert num_of_a_kind(roll, 3) == 10

def test_three_of_a_kind_not_found():
    roll = [1,4,6,5,2]
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    roll = [1,1,1,1,4]
    assert num_of_a_kind(roll, 4) == 8

def test_four_of_a_kind_not_found():
    roll = [1,1,3,4,3]
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    roll = [1,1,1,1,1]
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    roll = [1,1,3,4,3]
    assert yahtzee(roll) == 0



def test_all():
    test_four_of_a_kind_found()
    test_four_of_a_kind_not_found()
    test_three_of_a_kind_found()
    test_three_of_a_kind_not_found()
    test_yahtzee_found()
    test_yahtzee_not_found()

def main():
    print("Verifying functions", end="", flush=True)

    for _ in range(4):
        time.sleep(1)
        print(".", end="", flush=True)

    print("\nAll functions working!")

main()