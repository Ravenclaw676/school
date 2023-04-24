class Board(object):
    def __init__(self):
        print("no")


class Player (object):
    def __init__(self, number: int, game_board: Board):
        self._board = game_board
        self._number = number

    def get_number(self) -> int:
        return self._number

    def get_board(self) -> Board:
        return self._board

    def _get_row(self) -> int:
        return 0

    def _get_column(self) -> int:
        return 0

    def take_shot(self):
        x = self._get_row()
        y = self._get_column()
        self._board.take_shot(x, y)


board = Board()
player = Player(1, board)
player.get_board()
