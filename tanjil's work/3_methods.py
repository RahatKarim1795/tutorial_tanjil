#Method 1
matrix = []
rows = 3
cols = 4

for i in range(rows):
    a_row = []
    for j in range(cols):
        a_row.append(j)
    matrix.append(a_row)


#Method 2
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

new_board = []
for row in range(len(board)):
    new_row = []
    for col in range(len(board[row])):
        if (board[row][col]) % 2 == 0:
            new_row.append('X')
        else:
            new_row.append('O')
    new_board.append(new_row)

for i in new_board:
    print(i)

#Method 3
new_board = []

row_index = 0
for row in range(len(board)):
    new_row = []
    col_index = 0
    for col in range(len(board[0])):
        if (row_index + col_index) % 2 == 0:
            new_row.append('X')
        else:
            new_row.append('O')
        col_index += 1
    new_board.append(new_row)
    row_index += 1

for i in new_board:
    print(i)