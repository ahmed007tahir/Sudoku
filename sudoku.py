# import libraries here. Use the following ones only.
import time

# add your implementation of the required functions here



def main(board):
    def welcome_message():
        print('''
    
 █░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀    ▀▀█▀▀ █▀▀█    █▀▀ █░░█ █▀▀▄ █▀▀█ █░█ █░░█ █ 
 █▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀    ░░█░░ █░░█    ▀▀█ █░░█ █░░█ █░░█ █▀▄ █░░█ ▀ 
 ░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀    ░░▀░░ ▀▀▀▀    ▀▀▀ ░▀▀▀ ▀▀▀░ ▀▀▀▀ ▀░▀ ░▀▀▀ ▄
    
    ''')
    
    welcome_message()
    main_menu(board)
def main_menu(board):
    main_menu_choice = input('''


█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█    
    
Please select one of the following options:
  (a) Begin a New Game
  (b) Exit the program
  Your Response: ''')
    if main_menu_choice == 'a':
        print('\n')
        print_board(board)
        sub_menu(board)
    elif main_menu_choice == 'b':
            print('''
▀▀█▀▀ ░█─░█ ─█▀▀█ ░█▄─░█ ░█─▄▀ ░█▀▀▀█ 　 ░█▀▀▀ ░█▀▀▀█ ░█▀▀█ 　 ░█▀▀█ ░█─── ─█▀▀█ ░█──░█ ▀█▀ ░█▄─░█ ░█▀▀█ █ █ █ 
─░█── ░█▀▀█ ░█▄▄█ ░█░█░█ ░█▀▄─ ─▀▀▀▄▄ 　 ░█▀▀▀ ░█──░█ ░█▄▄▀ 　 ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█ ░█─ ░█░█░█ ░█─▄▄ ▀ ▀ ▀ 
─░█── ░█─░█ ░█─░█ ░█──▀█ ░█─░█ ░█▄▄▄█ 　 ░█─── ░█▄▄▄█ ░█─░█ 　 ░█─── ░█▄▄█ ░█─░█ ──░█── ▄█▄ ░█──▀█ ░█▄▄█ ▄ ▄ ▄''')
    else:
        print("\n\tInvalid Response!\n")
        main_menu(board)
def sub_menu(board):
    action = input('''\nWould you like to:
  (a) Have a go at solving the puzzle yourself?
  (b) Get the computer to solve it for you?
  (c) Return to the Main Menu?
  Your Response: ''')
    if action == 'a':
        start_time = time.time()
        human_play(board)
        print ("\nIt took you", time.time() - start_time, "seconds to fill in the board!")
        end_of_game(board)
    elif action == 'b':
        if computer_play(board) == True:
            start_time = time.time()
            print_board(board)
            print("The computer solved the puzzle in",counter, "moves!")
            print ("The computer solved the puzzle in", time.time() - start_time, "seconds.")
            end_of_game(board)
    elif action == 'c':
        main_menu(board)
    else:
        print("\n\tInvalid Response!\n")
        sub_menu(board)
def print_board(sudoku):    # Note: this version of print_board is only suitible to be used with a 3x3 sized sudoku board.
    print("\n\t  A   B   C   D   E   F   G   H   I\n"+"\t╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    for row in range(len(sudoku)):
        if row % 3 == 0 and row != 0:
            print("\t╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
        elif row == 0:
            None
        else:
            print("\t╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
        for column in range(len(sudoku[0])):
            if column == 0:
                print("      " + str(row+1) + " ║ " + str(sudoku[row][column]), end="")
            elif column % 3 == 0 and column != 0:
                print(" ║ " + str(sudoku[row][column]), end="")
            elif column == 8:
                print(" │ " + str(sudoku[row][column]) + " ║")
            else:
                print( " │ " + str(sudoku[row][column]) , end="")
    print("	╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n")
def update_board(board,value,row,col):
    board[row][col] = value
def computer_play(board):   # Gets the computer to solve the sudoku board
    global counter # keeps track of the number of moves made
    counter+=1
    find = unfilled(board)
    if not find:    # stopping condition for the recursion
        return True
    else:
        row, column = find
    for i in range(1,10):
        if is_valid(board, str(i), row, column):
            update_board(board, str(i), row, column)
            if computer_play(board):    # create a "save point" for the program to backtrack to
                return True
            board[row][column] = " "    # replace value with empty space upon backtracking
    return False
def human_play(board, moves = 0):
    coordinates = get_coordinate()
    row, column, undo = coordinates
    if undo:
        print("undo reached human_play")
        pass
    if board[row][column] != " ":
        print("This space is not empty, plaese try again!")
        human_play(board,moves)
    value = get_value()
    moves = moves + 1
    update_board(board,value,row, column)
    print_board(board)
    if current_state(board) == 1:
        human_play(board, moves)
    elif current_state(board) == 2:
        print('''

░█▀▀█ ░█▀▀▀█ ░█▄─░█ ░█▀▀█ ░█▀▀█ ─█▀▀█ ▀▀█▀▀ ░█─░█ ░█─── ─█▀▀█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀█ █    ░█──░█ ░█▀▀▀█ ░█─░█    ░█──░█ ░█▀▀▀█ ░█▄─░█ █ 
░█─── ░█──░█ ░█░█░█ ░█─▄▄ ░█▄▄▀ ░█▄▄█ ─░█── ░█─░█ ░█─── ░█▄▄█ ─░█── ░█─ ░█──░█ ░█░█░█ ─▀▀▀▄▄ ▀    ░█▄▄▄█ ░█──░█ ░█─░█    ░█░█░█ ░█──░█ ░█░█░█ ▀ 
░█▄▄█ ░█▄▄▄█ ░█──▀█ ░█▄▄█ ░█─░█ ░█─░█ ─░█── ─▀▄▄▀ ░█▄▄█ ░█─░█ ─░█── ▄█▄ ░█▄▄▄█ ░█──▀█ ░█▄▄▄█ ▄    ──░█── ░█▄▄▄█ ─▀▄▄▀    ░█▄▀▄█ ░█▄▄▄█ ░█──▀█ ▄''')
        print("\nIt took you" ,moves, "moves to solve the puzzle")
    elif current_state(board) == 3:
        print('''

▒█░░▒█ ▒█▀▀▀█ ▒█░▒█    ▒█░░░ ▒█▀▀▀█  ▒█▀▀▀█ ▒█▀▀▀ █ 
▒█▄▄▄█ ▒█░░▒█ ▒█░▒█    ▒█░░░ ▒█░░▒█  ░▀▀▀▄▄ ▒█▀▀▀ ▀ 
░░▒█░░ ▒█▄▄▄█ ░▀▄▄▀    ▒█▄▄█ ▒█▄▄▄█  ▒█▄▄▄█ ▒█▄▄▄ ▄''')
        print("\nIt took you" ,moves, "moves to fill the board")
def current_state(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == " ":
                state = 1
                return state
    for i in range(len(board)):
        for j in range(len(board)):
            if is_valid(board,board[i][j],i,j):
                state = 2
            else:
                state = 3
    return state
def get_value():
    while True:
        try:
            value = int(input("Please insert a value (0-9): "))
            if  0 < value < 10:
                return value
            else:
                print("Invalid response!")
                get_value()
        except:
            print("Invalid response!")
def get_coordinate():
    coordinate = input("\nPlease enter the coordinates: ").upper()
    x_axis = "ABCDEFGHI"
    y_axis = "123456789"
    undo = False
    if coordinate == "UNDO":
        print("you wish to undo")
        undo = True
         # add code for undoing
    while not (len(coordinate) == 2 and (((coordinate[0] in x_axis) and (coordinate[1] in y_axis)) or ((coordinate[1] in x_axis) and (coordinate[0] in y_axis)))):
        print("Invalid input, Please try again!")
        coordinate = input("\nPlease enter the coordinates: ").upper()
    if  (coordinate[0] in x_axis) and (coordinate[1] in y_axis):
        row = coordinate[1]
        column = coordinate[0]
    elif (coordinate[1] in x_axis) and (coordinate[0] in y_axis):
        row = coordinate[0]
        column = coordinate[1]    
    match column:
                case "A":
                    column = 1
                case "B":
                    column = 2
                case "C":
                    column = 3
                case "D":
                    column = 4
                case "E":
                    column = 5   
                case "F":
                    column = 6
                case "G":
                    column = 7
                case "H":
                    column = 8
                case "I":
                    column = 9
    row = int(row)
    column = int(column)
    return row-1,column-1,undo
def is_valid(board, number, row, col):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[row][col] != number:
                # Checking the column for the value Number
                if board[x][col] == number:
                    return False
                if board[row][y] == number:
                    return False
                if ((x // 3) == (row // 3)) and ((y // 3) == (col // 3)):
                    if board[x][y] == number:
                        return False
    return True
def unfilled(board):    # function iterated through the board and finds the first unfilled space
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == " ":
                return (row, column)
def end_of_game(board):
    board = copyboard
    user_response = input('''\n
    
▀▀█▀▀ ░█─░█ ─█▀▀█ ░█▄─░█ ░█─▄▀ ░█▀▀▀█    ░█▀▀▀ ░█▀▀▀█ ░█▀▀█    ░█▀▀█ ░█─── ─█▀▀█ ░█──░█ ▀█▀ ░█▄─░█ ░█▀▀█ █ █ █ 
─░█── ░█▀▀█ ░█▄▄█ ░█░█░█ ░█▀▄─ ─▀▀▀▄▄    ░█▀▀▀ ░█──░█ ░█▄▄▀    ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█ ░█─ ░█░█░█ ░█─▄▄ ▀ ▀ ▀ 
─░█── ░█─░█ ░█─░█ ░█──▀█ ░█─░█ ░█▄▄▄█    ░█─── ░█▄▄▄█ ░█─░█    ░█─── ░█▄▄█ ░█─░█ ──░█── ▄█▄ ░█──▀█ ░█▄▄█ ▄ ▄ ▄
    
    
    Please choose one of the following options:
        a) Return to the Main Menu.
        b) Exit the program.
        Your response: ''')
    if user_response == "a":
        main_menu(board)
    elif user_response == "b":
        return
    else:
        print("Invalid Response!")
        end_of_game(board)


if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    option = 3
    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')

    # add code here to solve the sudoku
    
   
    counter = 0     # innitialises the variable that will keep track of the number of moves made by the player & computer

    copyboard = [x[:] for x in sudoku]    # makes a duplicate of the board to enable resetting the board after the game
    main(sudoku)
