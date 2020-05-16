print("Enter cells:")  # Prints input prompt
all_in = input()  # Accepts input as 9 character str

# Take input string and convert to 3 x 3 matrix, and separate rows and columns and diagonals
row_1 = [all_in[i] for i in range(0, 3)]
row_2 = [all_in[i] for i in range(3, 6)]
row_3 = [all_in[i] for i in range(6, 9)]

col_1 = [all_in[i] for i in range(0, 9, 3)]
col_2 = [all_in[i] for i in range(1, 9, 3)]
col_3 = [all_in[i] for i in range(2, 9, 3)]

dia_1 = [all_in[0], all_in[4], all_in[8]]
dia_2 = [all_in[2], all_in[4], all_in[6]]

grid_rows = [row_1, row_2, row_3]  # List of rows for iteration
grid_cols = [col_1, col_2, col_3]  # List of columns for iteration
grid_dias = [dia_1, dia_2]  # List of diagonals for iteration

# Create booleans for final assessment of game state
x_win = False
o_win = False
draw_ = False
unfin_ = False
imposs_ = False

game_state = str()

#  Check for three in a row, X first then O

# X wins
for part in grid_rows:
    if part[0] == part[1] == part[2] == "X":
        x_win = True
    else:
        x_win = x_win

# O wins
for part in grid_rows:
    if part[0] == part[1] == part[2] == "O":
        o_win = True
    else:
        o_win = o_win

# Check for three in a col, X first then O
# X wins
for part in grid_cols:
    if part[0] == part[1] == part[2] == "X":
        x_win = True
    else:
        x_win = x_win

# O wins
for part in grid_cols:
    if part[0] == part[1] == part[2] == "O":
        o_win = True
    else:
        o_win = o_win

# Check for three in a diag, X first then O
# X wins
for part in grid_dias:
    if part[0] == part[1] == part[2] == "X":
        x_win = True
    else:
        x_win = x_win

# O wins
for part in grid_dias:
    if part[0] == part[1] == part[2] == "O":
        o_win = True
    else:
        o_win = o_win

# Check for impossible game due to too many turns
x_plays = 0
o_plays = 0
for part in grid_rows:
    for play in part:
        if play == "X":
            x_plays += 1
        elif play == "O":
            o_plays += 1

if abs(x_plays - o_plays) >= 2:
    imposs_ = True


# Calculate game_state

if x_win and o_win:
    imposs_ = True
    game_state = "Impossible"
elif o_win:
    game_state = "O wins"
elif x_win:
    game_state = "X wins"
elif imposs_:
    game_state = "Impossible"
elif "_" in all_in:
    game_state = "Game not finished"
else:
    game_state = "Draw"

# Create variable for game board bounds

bound_ = "---------"  # Top and bottom grid bounds

# Draw complete grid

print(bound_)
print("| " + row_1[0] + " " + row_1[1] + " " + row_1[2] + " " + " |")
print("| " + row_2[0] + " " + row_2[1] + " " + row_2[2] + " " + " |")
print("| " + row_3[0] + " " + row_3[1] + " " + row_3[2] + " " + " |")
print(bound_)
print(game_state)
