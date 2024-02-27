class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.max_health = max_health
        self.current_health = current_health


    
    def __str__(self) -> str:
        print(f"{self.name} ({self.current_health}/{self.max_health})")


    
    def lose_health(self, amount: int) -> None:
        if amount <= 0:
            pass
        elif amount > self.current_health:
            self.current_health = 0
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



def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")

main()