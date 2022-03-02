from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size, the number of ships, the player's name
    and the board type (player board or computer).
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add anymore ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_coordinate(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size -1)

def valid_coordinates(x ,y, board):
    """
    Split exception message. Then do board.guess!!!!!!!!!!
    """
    try:
        get_coords = board.board[x][y]
        if get_coords == ".":
            return  True
    except:
        print("Invalid guesses try again")
    return  False
    

def populate_board(board):
    for _ in range(board.num_ships):
        board.add_ship(random_coordinate(board.size), random_coordinate(board.size)) 



def make_row_guess():
    guess_row_player = input("Please guess row number: \n")
    try:
        guess_row_player_int = int(guess_row_player)
    except Exception as e:
        print("[" + guess_row_player + "] is not a number" )
        make_row_guess()
    else:
        return guess_row_player_int


def make_col_guess():
    guess_col_player = input("Please guess column number: \n")
    try:
        guess_col_player_int = int(guess_col_player)
    except Exception as e:
        print("[" + guess_col_player + "] is not a number" )
        make_col_guess()
    else:
        return guess_col_player_int

    

    
def play_game(computer_board, player_board):
    print_board(player_board)
    print_board(computer_board)
    row_guess = make_row_guess()
    col_guess = make_col_guess()

def print_board(board):
    print(f'{board.name}\'s board')
    for row in board.board:
        element_row = ""
        for element in row:
            element_row += "    " + element
        print(element_row)
        print("")
       


def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the scores and
    initialises the boards.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to BattleShip!")
    print(f" Boards size: {size}, number of ships {num_ships}")
    print(" Top left corner is row: 0, column: 0")
    print("-" * 35)
    player_name = input("Please enter name here:\n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    
    populate_board(player_board)
    populate_board(computer_board)

    play_game(computer_board, player_board)





new_game()




