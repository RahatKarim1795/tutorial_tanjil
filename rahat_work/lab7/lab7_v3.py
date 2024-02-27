import copy

def create_grid(filename: str) -> list[list[int]]:

    f = open(filename, "r" , encoding = "utf-8")
    row = f.readline()
    column = f.readline()

    grid = []

    for i in range(int(row)):

        inner_list = []

        for j in range(int(column)):

            value = f.readline().strip()
            inner_list.append(int(value))
        
        grid.append(inner_list)
    
    return grid
    

def display_grid(grid: list[list[int]]) -> None:

    for i in grid:
        for j in i:
            print(f'{j:9}',end="")
        print()


def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    neighbors_list = []

    total_rows = len(grid)
    total_columns = len(grid[0]) 

    # Check the eight possible neighbor positions around the given row and column
    neighbor_positions = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),(row, col + 1), (row + 1, col - 1),
        (row + 1, col), (row + 1, col + 1)
    ]

    for row, column in neighbor_positions:
        
        if (row>=0) and (row<total_rows) and (column>=0) and (column<total_columns):

            neighbors_list.append(grid[row][column])

    return neighbors_list


def land_estimate(list):

    avg = sum(list)//len(list)        

    return int(avg)


def fill_gaps(grid: list[list[int]]) -> list[list[int]]:

    row = 0
    column = 0

    new_grid = copy.deepcopy(grid)


    for inner_list in new_grid:
        column = 0
        for elements in inner_list:

            neighbour_list = []

            if elements == 0:

                neighbour_list = find_neighbor_values(new_grid, row, column)

                avg = sum(neighbour_list)//len(neighbour_list)
                new_grid[row][column] = avg

                # new_grid[row][column] = land_estimate(neighbour_list)

            column+=1

        row+=1

    return new_grid


def main() -> None:

    grid = create_grid("data_2.txt")
    print("SimCity land values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)


if __name__ == "__main__":
    main()



