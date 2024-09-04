from itertools import combinations_with_replacement, permutations
from collections import Counter

def generate_2d_list():
    target_sum = 9
    max_occurrences = 3
    num_lists = 9
    allowed_numbers = list(range(1, 10))
    
    # Find all combinations of numbers that sum to 9
    possible_triples = [
        combo for combo in combinations_with_replacement(allowed_numbers, 3)
        if sum(combo) == target_sum and combo != (3, 3, 3)
    ]
    
    # Expand to permutations to account for different orders
    possible_permutations = set()
    for triple in possible_triples:
        possible_permutations.update(permutations(triple))

    # Convert to a list and shuffle for random selection
    possible_permutations = list(possible_permutations)
    
    # Function to check if adding the new combo exceeds the occurrence limits
    def valid_addition(combo, count):
        temp_count = count.copy()
        temp_count.update(combo)
        if any(value > max_occurrences for value in temp_count.values()):
            return False
        return True

    # Attempt to fill the list while respecting limits on occurrences
    final_list = []
    occurrences = Counter()
    for combo in possible_permutations:
        if len(final_list) < num_lists and valid_addition(combo, occurrences):
            final_list.append(list(combo))
            occurrences.update(combo)
            if len(final_list) == num_lists:
                break

    return final_list

# To generate the list, call the function
result = generate_2d_list()
print(result)
