
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

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)





new_game()




