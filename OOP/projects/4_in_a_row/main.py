"""The main file of the four in a row game"""

class Player():
    """A class then encapsulates the player"""
    def __init__(self, player_name: str, player_number: int):
        self.__player_name = player_name
        self.__player_number = player_number

    def get_name(self) -> str:
        """Returns the name attribute of the class as a string"""
        return self.__player_name

    def get_number(self) -> int:
        """Returns the player number attribute of the class as an int"""
        return self.__player_number


class Board():
    """a class than encapsultes the board"""
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
        """checks if a given column is full"""
        total = 0
        for row in range(0, self.__rows):
            if self.__board[row][column] != 0:
                total += 1

        if total == self.__rows:
            return True
        return False

    def board_full(self) -> bool:
        """
        checks if the entire board is full by calling the column_full 
        until one of them is not full
        """
        for column in range(0, self.__columns):
            if not self.column_full(column):
                return False
        return True

    def get_width(self) -> int:
        """returns the number of columns as an int"""
        return self.__columns


board = Board(8, 8)
print(board)
