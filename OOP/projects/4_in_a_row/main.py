class Player(object):
    def __init__(self, player_name: str, player_number: int):
        self.__player_name = player_name
        self.__player_number = player_number

    def get_name(self) -> str:
        return self.__player_name

    def get_number(self) -> int:
        return self.__player_number


class Board(object):
    def __init__(self, columns: int, rows: int) -> None:
        self.__columns = columns
        self.__rows = rows
        self.__board = []
        for y in range(0, self.__columns):
            self.__board.append([])
            for x in range(0, self.__rows):
                self.__board[y].append(0)

    def __repr__(self) -> str:
        string = ""
        for row in self.__board:
            for column in row:
                string += str(column)
                string += " "
            string += "\n"

        return string

    def column_full(self, column: int) -> bool:
        total = 0
        for row in range(0, self.__rows):
            if self.__board[row][column] != 0:
                total += 1

        if total == self.__rows:
            return True
        return False

    def board_full(self) -> bool:
        for column in range(0, self.__columns):
            if not self.column_full(column):
                return False
        return True

    def get_width(self) -> int:
        return self.__columns


board = Board(8, 8)
print(board)
