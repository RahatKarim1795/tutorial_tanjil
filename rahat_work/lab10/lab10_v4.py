import random

def poke_statsa(name, att, defn):
     
    poke_a = [name, att, defn]
    print(poke_a[0])
    return poke_a


# Pokemon1 is an instance of Pokemon class
# print(pokemon1)

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

    # other.lose_health(net_damage)



    def is_alive(self) -> bool:
        if self.current_health>0:
            return True
        else:
            return False



    def revive(self) -> None:
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")

        # pokemon1.attempt_attack(pokemon2)


    def attempt_attack(self, other: "Pokemon") -> bool:

        # choose luck coefficient
        luck = random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3])
        
        # round to integer
        damage = int(self.attack * luck)
        
        # attack goes through only if damage is greater than defense
        if damage > other.defense:

            # actual damage is damage subtracted by defense of defending pokemon
            net_damage = damage - other.defense

            # subtract the net damage from current hp
            other.lose_health(net_damage)

        # if the defending pokemon is at 0 hp
        # check 50% revival chance and return
        if other.current_health <= 0:
            a = random.choice([1,2,3,4,5,6,7,8,9,10])
            if a<=5:
                return True
            else:
                return False
            # return  random.choice([True,False])

        # if defending pokemon alive no need revival chance
        else: 
            return False


def read_pokemon_from_file(filename: str) -> list[Pokemon]:

    pokemon_list = []

    with open(filename, "r", encoding="utf-8") as file:
        # Read all lines from the file
        all_pokemon_data = [line.strip().split('|') for line in file]

    # Randomly select the specified number of data entries
    selected_pokemon_data = random.sample(all_pokemon_data, 2)
    print(selected_pokemon_data)

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

    round = 1

    print(f"\nBattle has started!\n")

    while pokemon1.is_alive() and pokemon2.is_alive():

        #  when you call a method on an instance of a class 
        # (such as pokemon1.attempt_attack(pokemon2)), 
        # the instance itself is automatically passed as the 
        # first argument to the method.

        # 1st pokemon attacks
        # if revival chance is true, revive pokemon and show hp
        if(pokemon1.attempt_attack(pokemon2)):
            pokemon1.revive()
            print(pokemon1)

        # just show hp if no revive
        else:
            print(pokemon1)

        # 2nd pokemon attacks
        if(pokemon2.attempt_attack(pokemon1)):
            pokemon2.revive()
            print(pokemon2)
        else:
            print(pokemon2)

        print(f"Round {round} over!")

        # max 10 rounds allowed
        round+=1
        if round>=10:
            break
        
        # added to get some user interaction
        x = input("Go to next round? (y/n): ")
        while x.lower()!="y":
            if x.lower() == "y":
                continue
            else:
                x = input("Go to next round? (y/n): ")

    if pokemon1.is_alive():
        print(f"{pokemon1.name} has won the battle!")
    elif pokemon2.is_alive():
        print(f"{pokemon2.name} has won the battle!")


main()


# a = [1,2,3,4]
# b,c,d,e = a
# print(c) = 2