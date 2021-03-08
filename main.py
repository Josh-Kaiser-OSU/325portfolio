"""

"""
from os import system, name


class Game:
    """
    The game class implements a Light Up game.
    """

    def __init__(self, squares_per_row):
        """
        Params:
            squares_per_row - an integer that specifies the size of the board
        Returns:
            None
        Notes:
            Initializes the class
        """
        self.row_size = squares_per_row
        self.board = [[' ' for _ in range(self.row_size)]
                      for _ in range(self.row_size)]

    def __repr__(self):
        """
        Params:
            None
        Returns:
            The string representation of the board of the current game.
        Notes:
            Allows for the board to be printed with the print() function
        """
        string_repr = ''
        string_repr += ' ' + '_' * self.row_size * 2 + '\n'
        for idx, arr in enumerate(self.board):
            string_repr += '|'
            for item in arr:
                string_repr += item + ' '
            string_repr += '|' + str(self.row_size-idx) + '\n'
        string_repr += ' ' + '-' * self.row_size * 2 + '\n'
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        string_repr += ' '
        for idx in range(self.row_size):
            string_repr += alphabet[idx] + ' '
        return string_repr

    def place_squares(self):
        """
        Params:
            None
        Return:
            None
        Notes:
            Places the squares for a valid game
        """
        self.place('a3', '#')
        self.place('b2', '4')
        self.place('b6', '#')
        self.place('c7', '2')
        self.place('e1', '#')
        self.place('f2', '0')
        self.place('f6', '2')
        self.place('g5', '2')

    def place(self, location, item):
        """
        Params:
            location - The location on the board to place the item in chess notation
            item - a character that will be placed on the board
        Returns:
            None
        Notes:
            Utility function
        """
        row, column = self.convert_notation(location)
        self.board[row][column] = item

    def convert_notation(self, location):
        """
        Params:
            location - a string in chess notation
        Returns:
            Tuple(row, column)
        Notes:
            Used to convert chess notation to row, column
        """
        location.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        row = self.row_size - int(location[1])
        column = alphabet.index(location[0])
        return row, column

    def board_filled(self):
        """
        Params:
            None
        Returns:
            Boolean True if filled, False otherwise
        Notes:
            Used to verify the board has no empty spaces
        """
        for row_idx in range(self.row_size):
            for col_idx in range(self.row_size):
                if self.board[row_idx][col_idx] == ' ':
                    return False
        return True

    def play_game(self):
        """
        Params:
            None
        Returns:
            None
        Notes:
            Game loop: get's user input and responds accordingly until the user wins.
        """
        playing = True
        while playing:
            # Print the board
            print(self)

            # Check if the player won
            if self.valid_board() and self.board_filled():
                print("\t\t YOU WIN!\n")
                input("Press return to quit")
                return

            # Allow user to make a move
            self.user_choices()

            # Draw the light on the board for the current flashlight placements
            self.lighten_board()

            # Clear the screen
            for _ in range(2):
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')

    def is_valid_flash_placement(self, location):
        """
        Params:
            location - a string of chess notation for desired flashlight placement
        Returns:
            Boolean - True if the location is a valid placement of a flashlight, Flase otherwise
        Notes:
            Doesn't allow the placement of a flashlight on a nonempty space
        """
        row, column = self.convert_notation(location)
        if self.board[row][column] != ' ':
            return False
        else:
            return True

    def place_flashlight(self):
        """
        Params:
            None
        Returns:
            None
        Notes:
            Get's users desired flashlight placement and places flashlight if valid placement
        """
        placement = input(
            "Where do you want to place the flashlight?\nYour choice: ")
        if self.is_valid_flash_placement(placement):
            self.place(placement, '¥')

    def remove_flashlight(self):
        """
        Params:
            None
        Returns:
            None
        Notes:
            Get user input of flashlight to be removed and removes flashlight
        """
        placement = input(
            "What are the coordinates of the flashlight you want to remove?\nYour choice: ")
        row, column = self.convert_notation(placement)
        if self.board[row][column] == '¥':
            self.board[row][column] = ' '

    def user_choices(self):
        """
        Params:
            None
        Returns:
            None
        Notes:
            Asks user for what type of move they want to make and calls respective functions
        """
        choices = "Please make a selection:\n"
        choices += "p to place a flashlight\n"
        choices += "r to remove a flashlight\n"
        choices += "your choice: "
        user_choice = input(choices)
        if user_choice == 'p':
            self.place_flashlight()
        elif user_choice == 'r':
            self.remove_flashlight()
        else:
            print("Invalid input")

    def light_cross(self, row, col):
        """
        Params:
            row - the row where a flashlight is
            col - the column where the flashlight is
        Returns:
            none
        Notes:
            Lights up in horizontal and vertical directions until an obstacle is met.
            Obstacles: '1','2','3','4','#'
        """
        # flashlight left
        cur_col = col - 1
        while cur_col >= 0 and (self.board[row][cur_col] == ' ' or self.board[row][cur_col] == '≈'):
            self.board[row][cur_col] = '≈'
            cur_col -= 1
        # flashlight right
        cur_col = col + 1
        while cur_col < self.row_size and (self.board[row][cur_col] == ' ' or self.board[row][cur_col] == '≈'):
            self.board[row][cur_col] = '≈'
            cur_col += 1
        # flashlight top
        cur_row = row - 1
        while cur_row >= 0 and (self.board[cur_row][col] == ' ' or self.board[cur_row][col] == '≈'):
            self.board[cur_row][col] = '≈'
            cur_row -= 1
        # flashlight bottom
        cur_row = row + 1
        while cur_row < self.row_size and (self.board[cur_row][col] == ' ' or self.board[cur_row][col] == '≈'):
            self.board[cur_row][col] = '≈'
            cur_row += 1

    def lighten_board(self):
        """
        Params:
            None
        Returns:
            None
        Notes:
            Goes over entire board and lights up every flashlight's beams
        """
        # Clear every lit space to blank (important if a flashlight was removed)
        for row_idx, row in enumerate(self.board):
            for col_idx, item in enumerate(row):
                if item == '≈':
                    self.board[row_idx][col_idx] = ' '

        # Draws light for each flashlight on the board
        for row_idx, row in enumerate(self.board):
            for col_idx, item in enumerate(row):
                if item == '¥':
                    self.light_cross(row_idx, col_idx)

    def restriction_met(self, row, col):
        """
        Params:
            row - the row of the restriction
            col - the column of the restriction
        Returns:
            Boolean - True if the restriction is met, False otherwise
        Notes:
            Verifies the restriction cell is bordered by the appropriate number of flashlights
        """
        allowed_flashlights = int(self.board[row][col])
        flashlight_count = 0
        # left
        if col - 1 >= 0 and self.board[row][col-1] == '¥':
            flashlight_count += 1
        # right
        if col + 1 < self.row_size and self.board[row][col+1] == '¥':
            flashlight_count += 1
        # top
        if row - 1 >= 0 and self.board[row-1][col] == '¥':
            flashlight_count += 1
        # bottom
        if row + 1 < self.row_size and self.board[row+1][col] == '¥':
            flashlight_count += 1

        if flashlight_count == allowed_flashlights:
            return True
        else:
            return False

    def valid_board(self):
        """
        Params:
            None
        Return:
            Boolean - True if all restrictions met, False otherwise
        Notes:
            Verifies that each restriction square on the board has its restriction met
        """
        restriction_squares = '1234'
        for row_idx in range(self.row_size):
            for col_idx in range(self.row_size):
                if self.board[row_idx][col_idx] in restriction_squares and not self.restriction_met(row_idx, col_idx):
                    return False
        return True


if __name__ == "__main__":
    # The board size will be 7 by 7
    squares_per_row = 7
    this_game = Game(squares_per_row)

    # Place restricting squares
    this_game.place_squares()

    # Allow suer to play the game
    this_game.play_game()
