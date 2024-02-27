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
            print(f'{j:9}', end="")
        print()
        
def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    neighbors_list = []

    total_rows =  len(grid)
    total_columns = total_rows

    # Check the eight possible neighbor positions around the given row and column
    neighbor_positions = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),(row, col + 1), (row + 1, col - 1),
        (row + 1, col), (row + 1, col + 1)]
    
    

    for row, column in neighbor_positions:
        #omit the coordinates/positions that are out of bounds
        if (row>=0) and (row<total_rows) and (column>=0) and (column<total_columns):

            neighbors_list.append(grid[row][column])

    return neighbors_list
        
def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    new_grid = grid
    print(new_grid)

    return new_grid
    


def main() -> None:
    grid = create_grid("data_0.txt")
    print("SimCity Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    fill_gaps(grid)


if __name__ == "__main__":
    main()