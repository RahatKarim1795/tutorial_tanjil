MAP_FILE = 'arcadia_map.txt'

def load_map(map_file: str) -> list[list[str]]:

    # f = open(map_file, "r")

    # grid_map = []

    # row_line = f.readline()

    # while row_line:
    #     grid_map.append(row_line.strip())
    #     row_line = f.readline()
    # f.close()

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
        col = 0
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
            new_position = [player_position[0] - 1, player_position[1]]
            
            #display original map along with the new position
            original_grid = load_map(MAP_FILE)
            display_map(original_grid, new_position)

            # change the grid so previous position becomes *
            r = 0
            for i in grid:
                c = 0
                for j in i:
                    if j == "@":
                        grid[r][c] = '*'
                    c+=1
                r+=1

            r,c = player_position

            # make the new position into @
            grid[r][c] = '@'


        elif direction == 'south':
            new_position = [player_position[0] + 1 , player_position[1]]


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



        elif direction == 'west':
            new_position = [player_position[0] , player_position[1] - 1]
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


        elif direction == 'east':
            new_position = [player_position[0] , player_position[1] + 1]
            
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
            # r = new_position[0]
            # c = new_position[1]
            grid[r][c] = '@'

        
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




def main():

    grid_map = load_map(MAP_FILE)

    player_position = find_start(grid_map)

    r,c = player_position
    grid_map[r][c] = '@'

    display_map(grid_map, player_position)
    print()
    
    print(f'Type "help" for instructions\n')

    x = get_command()

    # keep taking inputs until
    while x!= 'escape':

        if x.lower() == 'escape':
            quit()

        elif x.lower() == 'show map':
            display_map(load_map(MAP_FILE), player_position)

        
        elif x.lower() == 'help':
            print(f'The objective is to reach the end of the cave. The map shows all the paths. The stars (*) denote the movable path. The dashes (-) denote walls. (S) is the starting position. The (@) denotes your current position. The (F) denotes finishing line\nMove commands:\nType north,south,east or west to move accordingly. Type show map to show the map again\nType "help" for instructions\n')


        elif x.lower() == 'go north':
            player_position = get_player_position(grid_map)
            move('north', player_position, grid_map)

        elif x.lower() == 'go south':
            player_position = get_player_position(grid_map)
            move('south', player_position, grid_map)

        elif x.lower() == 'go west':
            player_position = get_player_position(grid_map)
            move('west', player_position, grid_map)

        elif x.lower() == 'go east':
            player_position = get_player_position(grid_map)
            move('east', player_position, grid_map)

        else:
            print("I do not understand. Type again\n")


        x = get_command()


if __name__ == '__main__':
    main()
