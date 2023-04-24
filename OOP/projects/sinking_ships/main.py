class Board(object):
    def __init__(self, columns: int, rows: int, player_number: int):
        self.__columns = columns
        self.__rows = rows
        self.__player_number = player_number
        self.__board = []

        for row in range(0, rows - 1):
            self.__board.append([])
            for column in range(0, columns, - 1):
                self.__board[row].append("E")

    def get_width(self) -> int:
        return self.__columns
    
    def get_highs(self) -> int:
        return self.__rows
    
    def take_shot(self, x: int, y: int) -> bool:
        match self.__board[y][x]:
            case "E":
                self.__board[y][x] = "M"
                return True
            case "S":
                self.__board[y][x] = "H"
                return True
            case _:
                return False
            
    def place_ship(self, length: int, x: int, y: int, direction: str):
        if direction == "h":
            for i in range(0, length - 1):
                if self.__board[y][x + i] == "S":
                    raise Exception
                else:
                    self.__board[y][x + i] = "S"
        else:
            for i in range(0, length - 1):



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

    def _place_ships(self):
        pass


class human_player(Player):
    def _get_row(self) -> int:
        row = -1
        while row not in range(0, self._board.get_height() - 1):
            row = int(input(f"Please enter the row you want to shoot \
                                        {self._board.get_height()}")) - 1

        return row

    def _get_column(self) -> int:
        column = -1
        while column not in range(0, self._board.get_width() - 1):
            column = int(input(f"Please enter the column you want to shoot \
                                        {self._board.get_width()}")) - 1
        return column

    def take_shot(self):
        while True:
            x = self._get_row()
            y = self._get_column()
            if not self._board.take_shot(x, y):
                print("you can't shoot somewhere you have already shot.")
            else:
                break

    def _place_ships(self):
        for ship in range(2, 5):
            error = True
            while error:
                direction = ""
                while direction not in ["h", "v"]:
                    direction = input("What direction is the ship facing,\
                                      horizontal or vertical (h/v)").lower()
                x = self._get_column()
                y = self._get_row()
                try:
                    self._board.place_ship(ship, x, y, direction)
                except Exception:
                    print("Ships can not overlap, try again")
                error = False


board = Board()
player = Player(1, board)
player.get_board()
