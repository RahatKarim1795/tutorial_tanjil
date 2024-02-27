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

    total_rows =  len(grid)
    total_columns = total_rows

    # Check the eight possible neighbor positions around the given row and column
    neighbor_positions = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),(row, col + 1), (row + 1, col - 1),
        (row + 1, col), (row + 1, col + 1)]
    
    

    for row, column in neighbor_positions:
        # omit the coordinates/positions that are out of bounds
        if (row>=0) and (row<total_rows) and (column>=0) and (column<total_columns):

            neighbors_list.append(grid[row][column])

    return neighbors_list
    
def count_row_col(grid):
    row = 0
    row_max = 0
    col = 0
    col_max = 0

    grid = [ [1,1,34,124], [32,512,35,6], [12,44,22,1],[2,23,12,1]]

    for i in grid:        
        col = 0
        for j in i:
            col += 1

        row += 1
        

    print(f"Row: {row} \n Col: {col}")

    display_grid(grid)
            

def main() -> None:


    grid = create_grid("data_0.txt")
    print("SimCity Land Values: ")
    display_grid(grid)
    print(find_neighbor_values(grid, 1, 1))


if __name__ == "__main__":
    main()





