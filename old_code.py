# All of this is the old slower code using a 2d array to store the board.
# I updated the board storage to a dictionary for the faster bigO

def old_to_array(fen_string):
    fen_string = fen_string.split(" ")
    fen_array = fen_string[0].split("/")
    fen_string.pop(0)
    fen_array += fen_string
    output = []
    found_white_king = False
    found_black_king = False
    for i in range(8):
        row = []
        for k in range(len(fen_array[i])):
            if fen_array[i][k] == 'r' or fen_array[i][k] == 'n' or fen_array[i][k] == 'b' or fen_array[i][k] == 'q' \
                    or fen_array[i][k] == 'p' or fen_array[i][k] == 'R' or fen_array[i][k] == 'N' \
                    or fen_array[i][k] == 'B' or fen_array[i][k] == 'Q' or fen_array[i][k] == 'P':
                row.append(fen_array[i][k])
            elif fen_array[i][k] == 'K':
                row.append('K')
                found_white_king = True
            elif fen_array[i][k] == 'k':
                row.append('k')
                found_black_king = True
            else:
                row += ("-" * int(fen_array[i][k]))
        # if len(row) != 8:
        #     raise ValueError(f"Row {i + 1} has an invalid number of columns")
        output.append(row)
    # if len(output) != 8:
    #     raise ValueError(f"The board has an invalid number of rows")
    # if not (found_white_king and found_black_king):
    #     raise ValueError("The board is missing one or more kings")
    output.append(fen_string)
    return output


# takes the board data list and returns a string in the format of FEN
def old_to_fen(board_array):
    output = ""
    for row in board_array[:8]:
        empty_spaces = 0
        for square in row:
            if square == '-':
                empty_spaces += 1
            else:
                if empty_spaces != 0:
                    output += str(empty_spaces)
                    empty_spaces = 0
                output += square
        if empty_spaces != 0:
            output += str(empty_spaces)
        output += '/'
    output = output[:len(output) - 1]
    output += f" {board_array[8][0]} {board_array[8][1]} {board_array[8][2]} {board_array[8][3]} {board_array[8][4]}"
    return output


# This is the old code that finds threats using the 2d array
# I need to make new code that uses the dictionary
def old_threat_map(board_array, team_white=True):
    threats = [["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"],
               ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"],
               ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"],
               ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"]]
    if team_white:
        team = ['K', 'Q', 'R', 'N', 'B', 'P']
    else:
        team = ['k', 'q', 'r', 'n', 'b', 'p']
    for i in range(len(board_array[:8])):
        for k in range(len(board_array[:8][i])):
            if board_array[:8][i][k] == team[5]:
                threats = old_pawn_threats(board_array, team, i, k, team_white, threats)
            elif board_array[:8][i][k] == team[3]:
                threats = old_knight_threats(board_array, team, i, k, team_white, threats)
            elif board_array[:8][i][k] == team[2] or board_array[:8][i][k] == team[1]:
                threats = old_straight_threats(board_array, team, i, k, team_white, threats)
            elif board_array[:8][i][k] == team[0]:
                threats = old_king_threats(board_array, team, i, k, team_white, threats)
            if board_array[:8][i][k] == team[4] or board_array[:8][i][k] == team[1]:
                threats = old_diagonal_threats(board_array, team, i, k, team_white, threats)
    return threats


def old_pawn_threats(board_array, team, i, k, team_white, threats):
    if team_white:
        if k - 1 > -1 and board_array[:8][i - 1][k - 1] not in team:
            if threats[i - 1][k - 1] == "0":
                threats[i - 1][k - 1] = '1'
            else:
                threats[i - 1][k - 1] = '2'
        if k + 1 < 8 and board_array[:8][i - 1][k + 1] not in team:
            if threats[i - 1][k + 1] == "0":
                threats[i - 1][k + 1] = '1'
            else:
                threats[i - 1][k + 1] = '2'
    else:
        if k - 1 > -1 and board_array[:8][i + 1][k - 1] not in team:
            if threats[i + 1][k - 1] == "0":
                threats[i + 1][k - 1] = '1'
            else:
                threats[i + 1][k - 1] = '2'
        if k + 1 < 8 and board_array[:8][i + 1][k + 1] not in team:
            if threats[i + 1][k + 1] == "0":
                threats[i + 1][k + 1] = '1'
            else:
                threats[i + 1][k + 1] = '2'
    return threats


def old_knight_threats(board_array, team, i, k, team_white, threats):
    # Down 1 over 2
    if k - 1 > -1:
        if i - 2 > -1 and board_array[:8][i - 2][k - 1] not in team:
            if threats[i - 2][k - 1] == "0":
                threats[i - 2][k - 1] = '1'
            else:
                threats[i - 2][k - 1] = '2'
        if i + 2 < 8 and board_array[:8][i + 2][k - 1] not in team:
            if threats[i + 2][k - 1] == "0":
                threats[i + 2][k - 1] = '1'
            else:
                threats[i + 2][k - 1] = '2'
    # Down 2 over 1
    if k - 2 > -1:
        if i - 1 > -1 and board_array[:8][i - 1][k - 2] not in team:
            if threats[i - 1][k - 2] == "0":
                threats[i - 1][k - 2] = '1'
            else:
                threats[i - 1][k - 2] = '2'
        if i + 1 < 8 and board_array[:8][i + 1][k - 2] not in team:
            if threats[i + 1][k - 2] == "0":
                threats[i + 1][k - 2] = '1'
            else:
                threats[i + 1][k - 2] = '2'
    # Up 1 over 2
    if k + 1 < 8:
        if i - 2 > -1 and board_array[:8][i - 2][k + 1] not in team:
            if threats[i - 2][k + 1] == "0":
                threats[i - 2][k + 1] = '1'
            else:
                threats[i - 2][k + 1] = '2'
        if i + 2 < 8 and board_array[:8][i + 2][k + 1] not in team:
            if threats[i + 2][k + 1] == "0":
                threats[i + 2][k + 1] = '1'
            else:
                threats[i + 2][k + 1] = '2'
    # Up 2 over 1
    if k + 2 < 8:
        if i - 1 > -1 and board_array[:8][i - 1][k + 2] not in team:
            if threats[i - 1][k + 2] == "0":
                threats[i - 1][k + 2] = '1'
            else:
                threats[i - 1][k + 2] = '2'
        if i + 1 < 8 and board_array[:8][i + 1][k + 2] not in team:
            if threats[i + 1][k + 2] == "0":
                threats[i + 1][k + 2] = '1'
            else:
                threats[i + 1][k + 2] = '2'
    return threats


def old_straight_threats(board_array, team, i, k, team_white, threats):
    num = i - 1
    # Attack up
    while num > -1 and board_array[:8][num][k] not in team:
        if threats[num][k] == "0":
            threats[num][k] = '1'
        else:
            threats[num][k] = '2'
        if board_array[:8][num][k] != "-":
            break
        num -= 1
    num = i + 1
    # Attack down
    while num < 8 and board_array[:8][num][k] not in team:
        if threats[num][k] == "0":
            threats[num][k] = '1'
        else:
            threats[num][k] = '2'
        if board_array[:8][num][k] != "-":
            break
        num += 1
    num = k - 1
    # Attack right
    while num > -1 and board_array[:8][i][num] not in team:
        if threats[i][num] == "0":
            threats[i][num] = '1'
        else:
            threats[i][num] = '2'
        if board_array[:8][i][num] != "-":
            break
        num -= 1
    num = k + 1
    # Attack left
    while num < 8 and board_array[:8][i][num] not in team:
        if threats[i][num] == "0":
            threats[i][num] = '1'
        else:
            threats[i][num] = '2'
        if board_array[:8][i][num] != "-":
            break
        num += 1
    return threats


def old_king_threats(board_array, team, i, k, team_white, threats):
    # Left 1 Up/Down ?
    if k - 1 > -1:
        if board_array[:8][i][k - 1] not in team:
            if board_array[:8][i][k - 1] == "0":
                board_array[:8][i][k - 1] = '1'
            else:
                board_array[:8][i][k - 1] = '2'
        if i + 1 < 8 and board_array[:8][i + 1][k - 1] not in team:
            if threats[i + 1][k - 1] == "0":
                threats[i + 1][k - 1] = '1'
            else:
                threats[i + 1][k - 1] = '2'
        if i - 1 > -1 and board_array[:8][i - 1][k - 1] not in team:
            if threats[i - 1][k - 1] == "0":
                threats[i - 1][k - 1] = '1'
            else:
                threats[i - 1][k - 1] = '2'
    # Right 1 Up/Down ?
    if k + 1 < 8:
        if board_array[:8][i][k + 1] not in team:
            if threats[i][k + 1] == "0":
                threats[i][k + 1] = '1'
            else:
                threats[i][k + 1] = '2'
        if i + 1 < 8 and board_array[:8][i + 1][k + 1] not in team:
            if threats[i + 1][k + 1] == "0":
                threats[i + 1][k + 1] = '1'
            else:
                threats[i + 1][k + 1] = '2'
        if i - 1 > -1 and board_array[:8][i - 1][k + 1] not in team:
            if threats[i - 1][k + 1] == "0":
                threats[i - 1][k + 1] = '1'
            else:
                threats[i - 1][k + 1] = '2'
    # Down 1
    if i + 1 < 8 and board_array[:8][i + 1][k] not in team:
        print(i+1, k)
        print(board_array[:8][i + 1][k])
        if threats[i + 1][k] == "0":
            threats[i + 1][k] = '1'
        else:
            threats[i + 1][k] = '2'
    # Up 1
    if i - 1 > -1 and board_array[:8][i - 1][k] not in team:
        if threats[i - 1][k] == "0":
            threats[i - 1][k] = '1'
        else:
            threats[i - 1][k] = '2'
    return threats


def old_diagonal_threats(board_array, team, i, k, team_white, threats):
    num_i = i + 1
    num_k = k - 1
    # Attack down-right
    while num_i < 8 and num_k > -1 and board_array[:8][num_i][num_k] not in team:
        if threats[num_i][num_k] == "0":
            threats[num_i][num_k] = '1'
        else:
            threats[num_i][num_k] = '2'
        if board_array[:8][num_i][num_k] != "-":
            break
        num_i += 1
        num_k -= 1
    num_i = i - 1
    num_k = k - 1
    # Attack up-right
    while num_i > -1 and num_k > -1 and board_array[:8][num_i][num_k] not in team:
        if threats[num_i][num_k] == "0":
            threats[num_i][num_k] = '1'
        else:
            threats[num_i][num_k] = '2'
        if board_array[:8][num_i][num_k] != "-":
            break
        num_i -= 1
        num_k -= 1
    num_i = i + 1
    num_k = k + 1
    # Attack down-right
    while num_i < 8 and num_k < 8 and board_array[:8][num_i][num_k] not in team:
        if threats[num_i][num_k] == "0":
            threats[num_i][num_k] = '1'
        else:
            threats[num_i][num_k] = '2'
        if board_array[:8][num_i][num_k] != "-":
            break
        num_i += 1
        num_k += 1
    num_i = i - 1
    num_k = k + 1
    # Attack up-right
    while num_i > -1 and num_k < 8 and board_array[:8][num_i][num_k] not in team:
        if threats[num_i][num_k] == "0":
            threats[num_i][num_k] = '1'
        else:
            threats[num_i][num_k] = '2'
        if board_array[:8][num_i][num_k] != "-":
            break
        num_i -= 1
        num_k += 1
    return threats


# This is also old stuff that uses the 2d array
# takes the board data list and returns the score based on each player's remaining pieces
def old_piece_score(board_array):
    score = 0
    for row in board_array[:8]:
        for square in row:
            if square == '-':
                continue
            elif square == 'p':
                score -= 1
            elif square == 'P':
                score += 1
            elif square == 'r':
                score -= 4
            elif square == 'R':
                score += 4
            elif square == 'b':
                score -= 3
            elif square == 'B':
                score += 3
            elif square == 'n':
                score -= 3
            elif square == 'N':
                score += 3
            elif square == 'q':
                score -= 8
            elif square == 'Q':
                score += 8
    return score


def old_piece_score_dict(board_dict):
    score = 0
    for key in board_dict:
        a = 'a'
        if board_dict[key] == 'R':
            score += 4
        if board_dict[key] == 'r':
            score -= 4
        if board_dict[key] == 'B' or board_dict[key] == "N":
            score += 3
        if board_dict[key] == 'b' or board_dict[key] == "n":
            score -= 3
        if board_dict[key] == 'q':
            score += 8
        if board_dict[key] == 'Q':
            score -= 8
        if board_dict[key] == 'p':
            score += 1
        if board_dict[key] == 'P':
            score -= 1
    return score


def in_check(board_array):
    # Whites turn
    for i in range(8):
        for k in range(8):
            if board_array[8][0] == 'w':
                if board_array[i][k] == 'K' and old_threat_map(board_array, False)[i][k] == '1':
                    return 1
                elif board_array[i][k] == 'K' and old_threat_map(board_array, False)[i][k] == '2':
                    return 2
                return 0
            else:
                if board_array[i][k] == 'k' and old_threat_map(board_array, False)[i][k] == '1':
                    return 1
                elif board_array[i][k] == 'k' and old_threat_map(board_array, False)[i][k] == '2':
                    return 2
                return 0
    return -1