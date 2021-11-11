import unittest
import fen


class testFen(unittest.TestCase):
    def test_empty_board(self):
        fen_string = "8/8/8/8/8/8/8/8 w - - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_starting_board(self):
        fen_string = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_empty_end(self):
        fen_string = "rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/8 w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_empty_start(self):
        fen_string = "8/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_full_board(self):
        fen_string = "rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_missing_one_piece_from_row_end(self):
        fen_string = "rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbn1/rnbqkbnr/rnbqkbnr/rnbqkbnr w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_missing_four_pieces_from_row_end(self):
        fen_string = "rnbqkbnr/rnbq4/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_missing_four_pieces_from_row_middle(self):
        fen_string = "rnbqkbnr/rnbqkbnr/rnbqkbnr/rn4nr/rnbqkbnr/rnbqkbnr/rnbqkbnr/rnbqkbnr w KQkq - 0 1"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_1(self):
        fen_string = "8/1pq1R1k1/7p/p5p1/P7/2b2Q1P/1P1r1P2/1B5K b - - 0 37"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_2(self):
        fen_string = "r1br4/ppp3k1/n3pR2/2n1B3/5P2/2N5/PP4P1/2KR1BN1 b - - 4 23"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_3(self):
        fen_string = "8/2P5/8/3R4/5pk1/6p1/2r3K1/8 w - - 1 67"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_4(self):
        fen_string = "2qr1k1Q/p5p1/1p4P1/2p1bN2/2P1n3/1P6/P4P2/4R1K1 b - - 3 33"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_5(self):
        fen_string = "8/1p6/1k6/8/3p1K2/8/8/8 w - - 0 53"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)

    def test_random_board_6(self):
        fen_string = "5Q2/p5Rk/7p/p3p3/1P2P3/P3B2P/2q2PP1/6K1 b - - 0 37"
        result = fen.dict_to_fen(fen.fen_to_dict(fen_string))
        self.assertEqual(fen_string, result)


if __name__ == '__main__':
    unittest.main()
