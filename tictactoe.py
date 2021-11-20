import random, time
from func import slow_type

#1. drawing the board
board = dict(bl=' ',bc=' ',br=' ',ml=' ',mc=' ',mr=' ',tl=' ',tc=' ',tr=' ')

def drawboard(board:dict):
   print('•••••')
   print(board['tl']+'|'+board['tc']+'|'+board['tr'])
   print('-+-+-')
   print(board['ml']+'|'+board['mc']+'|'+board['mr'])
   print('-+-+-')
   print(board['bl']+'|'+board['bc']+'|'+board['br'])
   print('•••••')
   
   return board

#2.player choosing btn X and O
def choose_x_or_o():
   letter=""
   while not (letter=='X' or letter=='O'):
      print("will you be X or O??")
      letter=input().upper()
      
   if letter=='X':
      #print("you are X, the computer will be O")
      slow_type("you are X, the computer will be O")
      return ['X','0']
      
   else:
      #print("you are O, the computer will be X")
      slow_type("you are O, the computer will be X")
      return ['O','X']
      
#3.a coin flip on who starts the game      
def who_goes_first():
   if random.randint(0,1)==0:
      return 'Computer'
   else:
      return 'You'
      
#4. want to play again?
def play_again():
   print("do you want to play again?.. yes?")
   ans=input().lower()
   if ans in ['yes','y']:
      return True
   else:
      return False
      
#5.making a move 
def make_a_move(board,letter,move):
   board[move]=letter
   return board

#6.winning combinations
def is_winner(board):
   return (board['bl']==board['bc']==board['br'] and board['bc'] != " ") or (board['ml']==board['mc']==board['mr'] and board['ml'] != " ") or (board['tl']==board['tc']==board['tr'] and board['tl'] != " ") or (board['bl']==board['mc']==board['tr'] and board['bl'] != " ") or (board['bl']==board['ml']==board['tl'] and board['bl'] != " ") or(board['br']==board['mc']==board['tl'] and board['br'] != " ") or (board['br']==board['mr']==board['tr'] and board['br'] != " ") or (board['bc']==board['mc']==board['tc'] and board['bc'] != " ")
   
#7. a duplicate board
def get_board_copy(board:dict):
   dupeboard=board
   return dupeboard
   
#8. check if board space is free 
def is_space_free(board,move):
   return board[move]==" "
   
#9.let player type in their move
def get_player_move(board,player_letter):
   move=""
   while move not in board.keys():
      while move not in available_moves(board):
         slow_type("your turn to move..")
         print()
         move=str(input().lower())
         
         if is_space_free(board,move):
            print(f'oookaay..{repr(move.upper())} it is')
            board=make_a_move(board,player_letter,move)
            return board
                  
         else:
            slow_type("please choose an empty square.. this are your options")
            print()
            print(available_moves(board))
            
#10.list of available moves
def available_moves(board):
   possible_moves=[]
   for move in board.keys():
      if is_space_free(board,move):
         possible_moves.append(move)
   return possible_moves

"""   
#10.1 :choosing move from available options
def choose_random_move():
   lst=available_moves(board)
   move=random.choice(lst)
   return move
"""
"""
PART 2: 'CREATING THE COMPUTER AI'

steps:

First, see if there’s a move the computer can make that will win the game. If there is, take that move. Otherwise, go to the second step.

Second, see if there’s a move the player can make that will cause the computer to lose the game. If there is, the computer should move there to block the player. Otherwise, go to the third step.

Third, check if any of the corner spaces (spaces br, tr, tl, or bl) are free. If no corner space is free, then go to the fourth step.

Fourth, check if the center is free. If so, move there. If it isn’t, then go to the fifth step.

Fifth, move on any of the side pieces (spaces bc, ml, mr, or tc). There are no more steps, because if the execution has reached this step then the side spaces are the only spaces left.
"""
def get_AI_move(board,computer_letter):
   #1. check if it can win in one move
   for move in board.keys():
      duplicate_board=get_board_copy(board)
      
      if is_space_free(duplicate_board,move):
         dup_board=make_a_move(duplicate_board,computer_letter,move)
         
         if is_winner(dup_board):
            #drawboard(dup_board)
            #print('ended in 1',move)
            board=make_a_move(board,computer_letter,move)
            return board
            
         else:
            dup_board[move]=" "
            
   #2. check if the player can win in the next move
   for move in board.keys():
      duplicate_board=get_board_copy(board)
      if computer_letter=='X':
         player_letter='O'
      else:
         player_letter='X'
      if is_space_free(duplicate_board, move):
         duplicate_board=make_a_move(duplicate_board, player_letter,move)
         if is_winner(duplicate_board):
            #print('ended in 2',move)
            #drawboard(duplicate_board)
            board=make_a_move(board,computer_letter,move)
            return board
         else:
            duplicate_board[move]=" "
      
   #3. check if any corner space is free
   available_spaces=available_moves(board)
   try:
      corner_spaces=[]
      for move in available_spaces:
         if move in ['bl','br','tl','tr']:
            corner_spaces.append(move)
      move=random.choice(corner_spaces)
      #print(move,type(move)
      board=make_a_move(board,computer_letter,move)
      return board
   
   except:
      print('no corner spaces')
      
   #4 check if the centre is free
   if 'mc' in available_spaces:
      move='mc'
      board=make_a_move(board,computer_letter,move)
      return board 
   #. finally pick a side space
   else:
      side_spaces=[]
      for move in available_spaces:
         side_spaces.append(move)
      move=random.choice(side_spaces)
      board=make_a_move(board,computer_letter,move)
      return board
     
#finally: check if board is full
def is_board_full(board):
   if len(available_moves(board))<1:
      return True
   else:
      return False
      
#PLAYING THE game
while True:
   slow_type("welcome to the TICTACTOE competition..")
   print()
   board = dict(bl=' ',bc=' ',br=' ',ml=' ',mc=' ',mr=' ',tl=' ',tc=' ',tr=' ')
   player_letter,computer_letter=choose_x_or_o()
   turn=who_goes_first()
   print()
   print(f"{turn} will go first")
   
   """
   computer responses.. this is just for fun
           ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
   """
   ai_responses=[
      "I'm a dumb AI.. go slow on me",
      "oh!! okay!! i see you..",
      "These human games are ridiculous",
      "aaargh!!! i'm thinking.. chill",
      "wait.. am i X or O?..",
      "cant we just create a better game..",
      "for fuck sake!! my head is banging!",
      "goddamnit!! atleast try to win"
      ]
   
   game_is_playing=True
   
   while game_is_playing:
      if turn=="You":
         board=get_player_move(board,player_letter)
         drawboard(board)
         if is_winner(board):
            slow_type("You have won the game.. Congratulations")
            print()
            game_is_playing=False
            
         elif is_board_full(board):
            slow_type("it's a DRAW!!")
            game_is_playing=False
            
         else:
            turn='Computer'
         
   
      else:
         slow_type(random.choice(ai_responses))
         print()
         time.sleep(1.5)
         slow_type("here i go..")
         print()
         
         board=get_AI_move(board,computer_letter)
         drawboard(board)
         if is_winner(board):
            slow_type("You have lost to a very dump AI!!.. shame on you")
            print()
            game_is_playing=False
         elif is_board_full(board):
            slow_type("it's a DRAW!!")
            game_is_playing=False
         else:
            turn='You'
            
   if not play_again():
      break