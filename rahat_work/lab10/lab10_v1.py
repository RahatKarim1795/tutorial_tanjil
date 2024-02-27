class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.max_health = max_health
        self.current_health = current_health



def main():

    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")

main()