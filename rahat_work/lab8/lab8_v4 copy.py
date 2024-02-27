emojis = [("-", "🧱"), ("S", "🏠"), ("F", "🏺"), ("*", "🟢")]

MAP_FILE = 'arcadia_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:

    with open(map_file, "r") as f:
        grid_map = []

        for line in f:
            # Remove leading and trailing whitespace and split the line into a list of characters
            row = list(line.strip())
            grid_map.append(row)

    return grid_map


def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    row = 0
    col = 0

    for i in grid:
        col = 0
        for j in i:
            if player_position[0] == row and player_position[1] == col:
                print("@", end="")
            else:
                print(j, end="")
            col+=1
        print()
        row+=1
    print()


def find_start(grid: list[list[str]]) -> list[int, int]:
    
    row = 0
    col = 0

    for i in grid:
        for j in i:
            if j == "S":
                pos = [row,col]
            col+=1
        row+=1

    return pos


def get_command() -> str:
    x = input("Enter your move: ")

    return x


def get_grid_size(grid: list[list[str]]) -> list[int, int]:

    row = len(grid)
    col = len(grid[0])

    size = [row,col]
    
    return size


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:

    grid_rows, grid_cols = get_grid_size(grid)

    if (0<=position[0]< grid_rows) and (0<=position[1] < grid_cols):
        return True
    else:
        return False


def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')

    row = player_position[0]
    col = player_position[1]

    directions = []

    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')

    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')

    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')
    
    return directions
    
def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    
    allowed_moves = look_around(grid, player_position)

    if direction in allowed_moves:

        if direction == 'north':
            # get new position based on player move
            new_position = grid[player_position[0] - 1, player_position[1]]

            if check_finish(grid, new_position):
                print("Congratulations! You have reached the exit!")
                quit()

            else:
                #display original map along with the new position
                display_map(grid, new_position)

                print(f'You moved {direction}')

        elif direction == 'south':
            new_position = [player_position[0] + 1 , player_position[1]]

            if check_finish(grid, new_position):
                print("Congratulations! You have reached the exit!")
                quit()

            else:

                display_map(grid, new_position)

                print(f'You moved {direction}')


        elif direction == 'west':
            new_position = [player_position[0] , player_position[1] - 1]

            if check_finish(grid, new_position):
                print("Congratulations! You have reached the exit!")
                quit()

            else:   
                display_map(load_map(MAP_FILE), new_position)

                r = 0
                for i in grid:
                    c = 0
                    for j in i:
                        if j == "@":
                            grid[r][c] = '*'
                        c+=1
                    r+=1

                r,c = new_position
                grid[r][c] = '@'

                print(f'You moved {direction}')

        elif direction == 'east':
            new_position = [player_position[0] , player_position[1] + 1]

            if check_finish(grid, new_position):
                print("Congratulations! You have reached the exit!")
                quit()

            else:    
                display_map(grid, new_position)

                print(f'You moved {direction}')

        return True
    
    else:
        print(f'There is no way there, try again!')
        return False
    

def get_player_position(grid):
    r=0
    c=0
    for i in grid:
        c=0
        for j in i:
            if j == "@":
                return r,c
            c+=1
        r+=1

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    # TODO: implement this function
    r = 0
    c = 0
    for i in grid:
        c=0
        for j in i:
            if r==player_position[0] and c==player_position[1]:
                if grid[r][c] == "F":
                    return True
            c+=1
        r+=1
            
    return False

def show_start_map(grid):
    row = 0
    col = 0
    for i in grid:
        col = 0
        for j in i:
            print(j, end="")
            col+=1
        print()
        row+=1
    print()

def display_help():
    with open(HELP_FILE, "r") as h:
        for line in h:
            print(line.strip())

def make_step(grid_map, player_position):

    x = get_command()

    if x.lower() == 'escape':
        quit()

    elif x.lower() == 'show map':
        print("Map with your current position: \n")
        display_map(load_map(MAP_FILE), player_position)
    
    elif x.lower() == 'help':
        display_help()

    elif x.lower() == 'go north':
        player_position = get_player_position(grid_map)
        move('north', player_position, grid_map)

    elif x.lower() == 'go south':
        # player_position = get_player_position(grid_map)
        move('south', player_position, grid_map)

    elif x.lower() == 'go west':
        player_position = get_player_position(grid_map)
        move('west', player_position, grid_map)

    elif x.lower() == 'go east':
        player_position = get_player_position(grid_map)
        move('east', player_position, grid_map)

    else:
        print("I do not understand. Type again\n")

    make_step(grid_map, player_position)

def main():

    grid_map = load_map(MAP_FILE)

    player_position = find_start(grid_map)
    
    print("Game map:")
    show_start_map(grid_map)
    
    # r,c = player_position
    # grid_map[r][c] = '@'
    
    print(f'Type "help" for instructions\n')

    print("Game has started!")
    display_map(grid_map, player_position)

    make_step(grid_map, player_position)


if __name__ == '__main__':
    main()
