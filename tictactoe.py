#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys 
# The board is represented by a 2D list
board = [[' ' for _ in range(3)] for _ in range(3)] #the board is a 2d ist of empty spaces

# Function to print the Tic Tac Toe board
def print_board(): #to display current state of the board after each move 
    for row in board:
        print('|'.join(row)) #joins the elements of the row (which are empty spaces)using a |
        print('-' * 5) #separates rows with 5 dashes 


# In[2]:


#this fun runs every iteration to check if any winning condition is satisfied,doest check whom is winning
# Function to check if the game has ended
def game_over(): # checks if the game has ended by examining the rows,
    #columns, and diagonals of the board for winning combinations or a tie.
    # Check rows 
    #this function only returns true or false
    for row in board: #checks for all the rows in the board (3)      
        if row.count(row[0]) == 3 and row[0] != ' ': #the count() fun returns number of nonnull values
            return True                #not empty 

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ': #we have a win in a coloumn
            return True

    # Check diagonals
           #row,col
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # Check if the board is full
    if all(row.count(' ') == 0 for row in board):
        return True
     #else
    return False


# In[3]:


def evaluate():
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            if row[0] == 'X':
                return 1  #ai is winning,note that the ai plays with x
            else:
                return -1 #im winning

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            if board[0][col] == 'X':
                return 1
            else:
                return -1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        if board[0][0] == 'X':
            return 1
        else:
            return -1
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        if board[0][2] == 'X':
            return 1
        else:
            return -1
    return 0 #thats a tie


# In[ ]:


#this fun is the mind of the ai 
def minimax(is_maximizing): #we did all the prev functions to use in here ,is_maximizing is a boolean ,true if its the ai turn
    if game_over(): #checks if theres a winning condition,if game_over is true
        return evaluate() #who won?

    if is_maximizing: #the ai turn
        best_score = -sys.maxsize #the function initializes best_score with a very low value
        for row in range(3): 
            for col in range(3):
                if board[row][col] == ' ': 
                    board[row][col] = 'X'
                    score = minimax(False) 
                    board[row][col] = ' '
                    'X' from the cell (board[row][col] = ' ') to undo the move
                    best_score = max(score, best_score)
        return best_score
    else: #human turn 
        best_score = sys.maxsize
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(True) 
                    board[row][col] = ' '
                    best_score = min(score, best_score) #aims to minimize the score
        return best_score


# In[ ]:


# Function to find the best move for the AI player
def find_best_move(): 
    best_score = -sys.maxsize
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(False) #returns worse human play 
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


# In[ ]:


def play_game():
    while not game_over():
        print_board()
        player_row = int(input("Enter the row (0-2): "))
        player_col = int(input("Enter the column (0-2): "))
        if board[player_row][player_col] == ' ': #byt2akd en el mkan el user 3ayz ydkhl fih fady 
            board[player_row][player_col] = 'O'
            if not game_over():  
                print("AI is thinking...")
                ai_row, ai_col = find_best_move()
                board[ai_row][ai_col] = 'X'
            else:
                print_board()
                print("Game over!")
                break
        else:
            print("Invalid move. Try again.")

    print_board()
    score= evaluate()
    if score == 0:
        print("It's a tie!")
    elif score == 1:
        print("You win!")
    else:
        print("AI wins!")


# In[ ]:


# Start the game
play_game()


# In[ ]:





# In[ ]:




