from os import system, name


class Game:
    def __init__(self, squares_per_row):
        self.row_size = squares_per_row
        self.board = [[' ' for _ in range(self.row_size)]
                      for _ in range(self.row_size)]

    def __repr__(self):
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
        self.place('a3', '#')
        self.place('b2', '4')
        self.place('b6', '#')
        self.place('c7', '2')
        self.place('e1', '#')
        self.place('f2', '0')
        self.place('f6', '2')
        self.place('g5', '2')

    def place(self, location, item):
        row, column = self.convert_notation(location)
        self.board[row][column] = item

    def convert_notation(self, location):
        location.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        row = self.row_size - int(location[1])
        column = alphabet.index(location[0])
        return row, column

    def did_win(self):
        for row_idx in range(self.row_size):
            for col_idx in range(self.row_size):
                if self.board[row_idx][col_idx] == ' ':
                    return False
        return True

    def play_game(self):
        playing = True
        while playing:
            self.user_choices()
            self.lighten_board()
            if self.did_win():
                print("\t\t YOU WIN!\n")
                input("Press return to quit")
                return
            for _ in range(2):
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')
            print(self)

    def is_valid_flash_placement(self, location):
        row, column = self.convert_notation(location)
        if self.board[row][column] != ' ':
            return False
        else:
            return True

    def place_flashlight(self):
        placement = input(
            "Where do you want to place the flashlight?\nYour choice: ")
        if self.is_valid_flash_placement(placement):
            self.place(placement, '¥')

    def remove_flashlight(self):
        placement = input(
            "What are the coordinates of the flashlight you want to remove?\nYour choice: ")
        row, column = self.convert_notation(placement)
        if self.board[row][column] == '¥':
            self.board[row][column] = ' '

    def user_choices(self):
        choices = "Please make a selection:\n"
        choices += "p to place a flashlight\n"
        choices += "r to remove a flashlight\n"
        choices += "s to solve\n"
        choices += "your choice: "
        user_choice = input(choices)
        if user_choice == 'p':
            self.place_flashlight()
        elif user_choice == 'r':
            self.remove_flashlight()
        elif user_choice == 's':
            pass

    def light_cross(self, row, col):
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
        for row_idx, row in enumerate(self.board):
            for col_idx, item in enumerate(row):
                if item == '≈':
                    self.board[row_idx][col_idx] = ' '
        for row_idx, row in enumerate(self.board):
            for col_idx, item in enumerate(row):
                if item == '¥':
                    self.light_cross(row_idx, col_idx)


if __name__ == "__main__":
    squares_per_row = 7
    this_game = Game(squares_per_row)
    this_game.place_squares()
    print(this_game)
    this_game.play_game()
