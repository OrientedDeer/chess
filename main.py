from timeit import default_timer as timer
import fen

start = timer()
for i in range(1, 100000):
    fen_string = "r1br4/ppp3k1/n3pR2/2n1B3/5P2/2N5/PP4P1/2KR1BN1 b - - 4 23"
    result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
end = timer()
print(end - start, "Dict")

# todo
# 1. Find checks and prevent illegal moves
# 2. Add all legal moves to list
# 3. Make method that counts squares threatened
# 4. Make method that count pieces defended
# 5. Idea for method that checks how "open" the king is
