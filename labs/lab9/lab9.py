"""
Name: Nia Covington
lab9.py
TicTacToe
I certify this is my own work.
"""


def build_board():
    start_list=[1,2,3,4,5,6,7,8,9]
    return start_list

def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    valid_pst=str(board[position-1]).isnumeric()
    if valid_pst:
        return True
    else:
        return False

def fill_spot(board, position, character):
    new_char=character.strip().lower()
    board[position-1]=new_char

def winning_game(board):
    if board[1]==board[2]==board[3]:
        return True
    if board[4]==board[5]==board[6]:
        return True
    if board[7]==board[8]==board[9]:
        return True
    if board[1]==board[4]==board[7]:
        return True
    if board[2]==board[5]==board[8]:
        return True
    if board[3]==board[6]==board[9]:
        return True
    if board[1]==board[5]==board[9]:
        return True
    if board[3]==board[5]==board[7]:
        return True
    else:
        return False



def game_over(board):
    if winning_game(board):
        return True
    for space in board:
        if str(space).isnumeric():
            return False
    return True

def get_winner(board):
    if not game_over(board):
        return None
    if board.count("x") > board.count("o"):
        return "x"
    else:
        return "o"

def play(board):
    print("Welcome to Tic-Tac-Toe!")
    print("Two players take turns putting either x's and o's in empty positions. The first player to get three in a row"
          "wins! The game starts with x's")
    build_board()
    print_board(board)
    i=1
    player=fill_spot()
    while True:
        winning_game()
    # playAgain=input("Do you want to play again (y/n)?")
    # if playAgain=='Y' or 'y':
    #     return True
    # if playAgain=='N' or 'n':
    #     return False




def main():
    pass


if __name__ == '__main__':
    main()
