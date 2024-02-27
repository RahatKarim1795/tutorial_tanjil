"""
This program converts a set of data into a grid format where it shows the values of land.
Author: Tanjil Sarker Rafi
When: November 10, 2023
"""
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

    new_grid = copy.deepcopy(grid)
    row = 0 
    col = 0
    neighbour_list = []

    for i in grid:
        col = 0
        for j in i:
            if j == 0:
                neighbour_list = find_neighbor_values(new_grid,row,col)
                avg = sum(neighbour_list) / len(neighbour_list)
                new_grid[row][col] = round(avg)
            col += 1
        row += 1
    
    return new_grid


def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    
    grid_max = grid[0][0]
    for i in grid:
        for j in i:
            new_val = 0
            if j > grid_max:
                grid_max = j
            
    return grid_max
            


def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    sum_d = 0
    count = 0
    for i in grid:
        for j in i:
            sum_d += j
            count += 1
    
    avg = sum_d / count 
    
            
    
    return round(avg)
            


def main() -> None:
    grid = create_grid("data_3.txt")
    print("SimCity Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    fill_gaps(grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

    
main()
