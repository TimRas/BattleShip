from random import randint
import keyboard

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
        self.hits = 0

    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
    

        if (x, y) in self.ships:
            self.board[x][y] = "O"
            self.hits += 1
            if self.hits == self.num_ships:
                return "Win!"
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

def valid_coordinates(x, y, board):  
    try:
        get_coords = board.board[x][y]
        if get_coords == "." or get_coords == "@":
            return True
        else:
            print("You've already hit this position!")      
    except Exception as _:
        print(f"Guess is out of bounds, try again")
    return False
    

def populate_board(board):
    for _ in range(board.num_ships):
        board.add_ship(random_coordinate(board.size), random_coordinate(board.size)) 



def make_row_guess():
    guess_row_player = input("Please guess row number: \n")
    try:
        guess_row_player_int = int(guess_row_player)
    except Exception as e:
        print("[" + guess_row_player + "] is not a number" )
        return make_row_guess()
    else:
        return guess_row_player_int


def make_col_guess():
    guess_col_player = input("Please guess column number: \n")
    try:
        guess_col_player_int = int(guess_col_player)
    except Exception as e:
        print("[" + guess_col_player + "] is not a number" )
        return make_col_guess()
    else:
        return guess_col_player_int

    

    
def play_game(computer_board, player_board):
    print_board(player_board)
    print_board(computer_board)
    player_result = ask_player_guess(computer_board)
    computer_result = generate_computer_guess(player_board)
    next_round(player_result, computer_result, player_board, computer_board)
    

def ask_player_guess(computer_board):
    player_row_guess = make_row_guess()
    player_col_guess = make_col_guess()
    while not(valid_coordinates(player_row_guess, player_col_guess, computer_board)): 
        player_row_guess = make_row_guess()
        player_col_guess = make_col_guess()
    return computer_board.guess(player_row_guess, player_col_guess)

def generate_computer_guess(player_board):
    computer_row_guess = random_coordinate(player_board.size)
    computer_col_guess = random_coordinate(player_board.size)
    while not(valid_coordinates(computer_row_guess, computer_col_guess, player_board)):
        computer_row_guess = random_coordinate(player_board.size)
        computer_col_guess = random_coordinate(player_board.size)
    return player_board.guess(computer_row_guess, computer_col_guess)

def next_round(player_result, computer_result, player_board, computer_board):
    player_row_guess, player_col_guess = computer_board.guesses[len(computer_board.guesses) -1]
    computer_row_guess, computer_col_guess = player_board.guesses[len(player_board.guesses) -1] 
    print(f"{player_board.name} guessed: [{player_row_guess}, {player_col_guess}] ")
    print(f"{player_board.name}'s shot resulted in a {player_result}")
    print(f"Computer guessed: [{computer_row_guess}, {computer_col_guess}]")
    print(f"Computer's shot resulted in a {computer_result}")
    if computer_board.hits == computer_board.num_ships or player_board.hits == player_board.num_ships:
        print("")
        continue_game = input("If you want to play again, input: y. Otherwise input anything else.\n")
        if continue_game == "y":
            new_game()
        else:
            quit()
    else:
        play_game(computer_board, player_board)

        # while True:  # making a loop
        #         if keyboard.is_pressed('y'):  # if key 'q' is pressed 
        #             new_game()
        #             break  # finishing the loop
        #         elif keyboard.is_pressed('n'):
        #             quit()
            

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




