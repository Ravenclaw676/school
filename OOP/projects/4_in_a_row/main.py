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
        for column_number in range(0, self.__columns):
            self.__board.append([])
            for _ in range(0, self.__rows):
                self.__board[column_number].append(0)

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

    def add_token(self, player: Player, column: int) -> str:
        """adds a token to the first non empty row in the specified column"""
        if not self.column_full(column):
            for row in range(self.__rows - 1, 0, -1):
                if self.__board[row][column] == 0:
                    self.__board[row][column] = player.get_number()
                    return "done"
        else:
            return "column full"

    def check_winner(self) -> int:
        """checks all directions on the board and returns the player number if 4 in a row has been formed"""
        #vertical_result = self.check_vertical()
        #if vertical_result != 0:
        #    return vertical_result

        horizontal_result = self.check_horizontal()
        if horizontal_result != 0:
            return horizontal_result

        #right_diagonal_result = self.check_right_diagonal()
        #if right_diagonal_result != 0:
        #    return right_diagonal_result

        #left_diagonal_result = self.check_left_diagonal()
        #if left_diagonal_result != 0:
        #    return left_diagonal_result

    def check_horizontal(self) -> int:
        """checks all vertical columns for a 4 in a row and returns the winner"""
        for row in reversed(self.__board):
            last_value = 0
            number_in_a_row = 0
            for value in row:
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value

board = Board(8, 8)
player1 = Player("andrew", 1)
board.add_token(player1, 0)
board.add_token(player1, 1)
board.add_token(player1, 2)
board.add_token(player1, 3)
print(board)
print(board.check_winner())
