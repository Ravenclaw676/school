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

    def get_column(self) -> int:
        """returns the width of the board"""
        return self.__columns

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
        return "column full"

    def check_winner(self) -> int:
        """
        checks all directions on the board and returns the player number if 4
        in a row has been formed
        """
        vertical_result = self.check_vertical()
        if vertical_result != 0:
            return vertical_result

        horizontal_result = self.check_horizontal()
        if horizontal_result != 0:
            return horizontal_result

        right_diagonal_result = self.check_right_diagonal()
        if right_diagonal_result != 0:
            return right_diagonal_result

        left_diagonal_result = self.check_left_diagonal()
        if left_diagonal_result != 0:
            return left_diagonal_result

        return 0

    def check_vertical(self) -> int:
        """
        checks all vertical columns for 4 in a row and returns the player
        number of of the player who achived this
        """
        for column in range(0, self.__columns):
            last_value = 0
            number_in_a_row = 0
            for row in range(0, self.__rows):
                value = self.__board[row][column]
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value
                    number_in_a_row = 1
        return 0

    def check_horizontal(self) -> int:
        """
        checks all the horizontal rows for a 4 in a row and returns the player
        number of the player who achived this
        """
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
                    number_in_a_row = 1
        return 0

    def check_right_diagonal(self):
        """
        i hate this functions
        """
        last_value = 0
        number_in_a_row = 0
        initial_row = 0
        initial_column = 0
        while initial_row < self.__rows:
            for row, column in zip(range(initial_row, self.__rows),
                                   range(0, self.__columns)):
                value = self.__board[row][column]
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value
                    number_in_a_row = 1
            initial_row += 1

        while initial_column < self.__columns:
            for row, column in zip(range(0, self.__rows),
                                   range(initial_column, self.__columns)):
                value = self.__board[row][column]
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value
                    number_in_a_row = 1
            initial_column += 1

        return 0

    def check_left_diagonal(self) -> int:
        """
        i hate this functions
        """
        reversed_board = self.__board[::-1]

        last_value = 0
        number_in_a_row = 0
        initial_row = 0
        initial_column = 0
        while initial_row < self.__rows:
            for row, column in zip(range(initial_row, self.__rows),
                                   range(0, self.__columns)):
                value = reversed_board[row][column]
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value
                    number_in_a_row = 1
            initial_row += 1

        while initial_column < self.__columns:
            for row, column in zip(range(0, self.__rows),
                                   range(initial_column, self.__columns)):
                value = reversed_board[row][column]
                if value == last_value and number_in_a_row == 3:
                    return value
                elif value != 0 and value == last_value:
                    number_in_a_row += 1
                elif value != 0 and value != last_value:
                    last_value = value
                    number_in_a_row = 1
            initial_column += 1

        return 0


def drop_token(player: Player, game_board: Board) -> None:
    """
    a board that handles the dropping of tokens in relation to the userinput
    """
    print("Player", player.get_number(), "'s turn")
    while True:
        try:
            column = int(
                input("Please enter the column you want to drop a piece: "))
            break
        except ValueError:
            print("Please enter a number")

    while column not in range(game_board.get_column() + 1):
        try:
            print("please an enter a number within the bounds of the board")
            column = int(
                input("Please enter the column you want to drop a piece: "))
        except ValueError:
            print("please enter a number")

    column -= 1
    game_board.add_token(player, column)


def main() -> None:
    """the main function of 4 in a row"""
    player1_name = input("Player 1's name is: ")
    player2_name = input("Player 2's name is: ")
    player1 = Player(player1_name, 1)
    player2 = Player(player2_name, 2)

    board_width = 0
    while board_width <= 4:
        try:
            board_width = int(input("Please enter the board's width: "))
        except ValueError:
            print("Please enter a number")
    board_height = 0
    while board_height <= 4:
        try:
            board_height = int(input("Please enter the board's height: "))
        except ValueError:
            print("Please enter a number: ")
    board = Board(board_width, board_height)

    winner = 0
    while not board.board_full():
        drop_token(player1, board)
        print(board)
        if board.check_winner() != 0:
            winner = board.check_winner()
            break
        drop_token(player2, board)
        print(board)
        if board.check_winner() != 0:
            winner = board.check_winner()
            break

    print(board)
    print("Game over!")
    if board.board_full():
        print("Tie, the board was full and nobody got 4 in a rrow")
    elif winner == 1:
        print(player1.get_name(), " wins")
    elif winner == 1:
        print(player2.get_name(), "wins")


if __name__ == "__main__":
    main()
