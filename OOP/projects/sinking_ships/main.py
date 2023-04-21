class Board(object):
    def __init__(self):
        print("no")

class Player (object):
    def __init__(self, number: int, board: Board):
        self._board = board
        self._number = number

    def get_board(self) -> Board:
        return self._board


board = Board()
player = Player(1, board)
player.get_board()