MAP_FILE = 'arcadia_map.txt'

def load_map(map_file: str) -> list[list[str]]:

    f = open(map_file, "r")

    grid_map = []

    row_line = f.readline()

    while row_line:
        grid_map.append(row_line)
        row_line = f.readline()

    f.close()

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
    # """
    # Returns the size of the grid.
    # """
    # # # method 1
    # row = 0
    # col = 0
    # for i in grid:
    #     row+=1
    #     col = 0
    #     for j in i:
    #         col+=1
        
    # size = [row,col]



    # method 2

    # row = len(grid)
    # for inner_list in grid:
    #     col = len(inner_list)

    # size = [row,col]

    # # method 3
    row = len(grid)
    col = len(grid[0])

    size = [row,col]
    
    return size


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)

    if position[0]< grid_rows and position[1] < grid_cols:
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
    



def main():

    grid_map = load_map(MAP_FILE)

    start = find_start(grid_map)

    player_position = start

    display_map(grid_map, start)

    print()
    
    print(f'Type "help" for instructions\n')

    x =  get_command()

    if x.lower() == 'escape':
        quit()

    elif x.lower() == 'show map':
        display_map(load_map(MAP_FILE), player_position)
        get_command()
    
    elif x.lower() == 'help':
        print(f'The objective is to reach the end of the cave. The map shows all the paths. The stars (*) denote the movable path. The dashes (-) denote walls. (S) is the starting position. The (@) denotes your current position. The (F) denotes finishing line\nMove commands:\nType north,south,east or west to move accordingly. Type show map to show the map again\nType "help" for instructions\n')
        get_command()

    else:
        print("I do not understand. Type again")
        get_command()


if __name__ == '__main__':
    main()
