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
    if x.lower() == 'escape':
        quit()
    else:
        print("I do not understand. Type again")
        get_command()

    return x



def main():

    grid_map = load_map(MAP_FILE)

    for i in grid_map:
        for j in i:
            print(j, end="")

    print()
    get_command()


    # grid = [['A','*'],['*','S']]

    # start_position = find_start(grid)
    # print(find_start(grid))

if __name__ == '__main__':
    main()
