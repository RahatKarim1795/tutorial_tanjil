import random

def poke_statsa(name, att, defn):
     
    poke_a = [name, att, defn]
    print(poke_a[0])
    return poke_a


class Pokemon:
    
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.max_health = max_health
        self.current_health = current_health

    
    def __str__(self) -> str:
        return f"{self.name} ({self.current_health}/{self.max_health})"
    
    def lose_health(self, amount: int) -> None:
        if amount <= 0:
            return
        elif amount > self.current_health:
            self.current_health -= 0
        else:
            self.current_health -= amount



    def is_alive(self) -> bool:
        if self.current_health>0:
            return True
        else:
            return False



    def revive(self) -> None:
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")


def read_pokemon_from_file(filename: str) -> list[Pokemon]:

    pokemon_list = []

    with open(filename, "r", encoding="utf-8") as file:
        # Read all lines from the file
        all_pokemon_data = [line.strip().split('|') for line in file]

    # Randomly select the specified number of data entries
    selected_pokemon_data = random.sample(all_pokemon_data, 2)

    # Create Pokemon objects using the extracted data
    for data in selected_pokemon_data:

        # Check if the line has enough values
        if len(data) == 4:

            # Put the four values of the list into four variables
            namef, attackf, defensef, healthf = data

            # Set both max_health and current_health to the initial "Health" value
            pokemon_object = Pokemon(
                namef,
                int(attackf),
                int(defensef),
                int(healthf),
                int(healthf)
            )

            pokemon_list.append(pokemon_object)


    return pokemon_list

    




def main():
    """
    Battle of two Pokemon

    """

    poke_vs = read_pokemon_from_file("all_pokemon.txt")

    pokemon1 = Pokemon(poke_vs[0].name, 55, 40, 35, 35)
    pokemon2 = Pokemon(poke_vs[1].name, 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")


main()


# a = [1,2,3,4]
# b,c,d,e = a
# print(c) = 2