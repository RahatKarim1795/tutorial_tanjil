# def create_grid(filename: str) -> list[list[int]]:

#     f = open(filename, "r" , encoding = "utf-8")
#     row = f.readline()
#     column = f.readline()

#     grid = [[]]
#     inner_list = []
#     x = 0
#     y = 0

#     for i in range(int(row)):
#         for j in range(int(column)):

#             grid.append(f.readline())
        
#         inner_list = ""

#         # print(grid)


#     print(grid)

def create_grid(filename: str) -> list[list[int]]:

    f = open(filename, "r" , encoding = "utf-8")
    row = f.readline()
    column = f.readline()



    grid = []

    for i in range(int(row)):

        inner_list = []

        for j in range(int(column)):

            value = f.readline()

            inner_list.append(int(value))
        
        grid.append(inner_list)
    
    return grid
    

def display_grid(grid: list[list[int]]) -> None:

    for i in grid:
        for j in i:
            print(f'{j:9}',end="")
        print()
    

def main() -> None:


    grid = create_grid("data_0.txt")
    print("SimCity Land Values: ")
    display_grid(grid)

# main()


