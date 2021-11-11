# https://en.wikipedia.org/wiki/Forsyth-Edwards_Notation
import math

def fen_to_dict(fen_string):
    board_dict = {}
    index = 0
    fen_string = fen_string.split(' ')
    for character in fen_string[0]:
        if character.isdigit():
            index += int(character)
        elif character != '/':
            board_dict[index] = character
            index += 1
    board_dict[64] = f"{fen_string[1]} {fen_string[2]} {fen_string[3]} {fen_string[4]} {fen_string[5]}"
    return board_dict


def dict_to_fen(board_dict):
    fen = ""
    index = -1
    for key in board_dict:
        index_8_minus_mod = 8 - ((index + 1) % 8)
        if key == 64:
            continue
        if key == index + 1 and not math.floor(key/8) > math.floor(index/8):
            fen += board_dict[key]
        elif index != -1 and math.floor(key/8) > math.floor(index/8):
            if (index + 1) % 8 != 0 and math.floor(key/8) - math.floor(index/8) == 1:
                fen += str(index_8_minus_mod) + '/'
                index += index_8_minus_mod
            elif math.floor(key/8) - math.floor(index/8) > 1:
                if index_8_minus_mod != 0 and index_8_minus_mod != 8:
                    fen += str(index_8_minus_mod)
                fen += '/8'*(math.floor(key/8) - math.floor(index/8)-1)
                fen += '/'
                if key % 8 != 0 and key % 8 != 8:
                    fen += str(key % 8)
            else:
                fen += '/'
            if key - 1 - index != 0 and math.floor(key/8) - math.floor(index/8) <= 1:
                fen += str(key - 1 - index)
            fen += board_dict[key]
        else:
            if math.floor(key/8) > math.floor((index+1)/8):
                fen += f"8/"
                if key % 8 != 0 and key % 8 != 8:
                    fen += str(key % 8)
                fen += f"{board_dict[key]}"
            else:
                if key-1-index != 0:
                    fen += str(key-1-index)
                fen += board_dict[key]
        index = key
    if math.ceil((index+1)/8) != 8:
        if index != -1:
            if index_8_minus_mod != 8 and index_8_minus_mod != 0:
                fen += str(index_8_minus_mod)
            fen += '/8'*(8 - math.ceil((index + 1)/8))
        else:
            fen += '8'
            fen += '/8' * (7 - math.ceil((index + 1) / 8))
    elif index_8_minus_mod != 0 and index_8_minus_mod != 8:
        fen += str(index_8_minus_mod)
    fen += f" {board_dict[64]}"
    return fen
