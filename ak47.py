import random,time
from cards import Deck
from func import slow_type
from func import slow_type_mod as stm

class Drawings:
   def __init__(self):
      self.suits=dict(diamonds="♦",spades="♠",hearts="♥",clubs="♣")
      
   def draw_table(self, d:list):
      icon=self.suits.get(d[1])
      
      stm("*********************")
      stm("|    +--+   +--+     |")
      stm(f"|    |{d[0]}{icon}|   |??|     |")
      stm("|    +--+   +--+     |")
      stm("*********************")
      
   def draw_hand(self,h:list):
      i=[]
      for icon in h:
         i.append(icon[1])
         
      icon=self.suits.get
      
      stm("••••••••••••••••••••••••••••••")
      stm("|  +--+  +--+  +--+  +--+    |")
      stm(f"|  |{h[0][0]}{icon(i[0])}|  |{h[1][0]}{icon(i[1])}|  |{h[2][0]}{icon(i[2])}|  |{h[3][0]}{icon(i[3])}|    |")
      stm("|  +--+  +--+  +--+  +--+    |")
      stm("••••••••••••••••••••••••••••••")
      
   def draw_drop_options(self,h:list):
      i=[]
      for icon in h:
         i.append(icon[1])
         
      icon=self.suits.get
      
      stm("××××××××××××××××××××××××××××××××××××")
      stm("|  +--+  +--+  +--+  +--+  +--+    |")
      stm(f"|  |{h[0][0]}{icon(i[0])}|  |{h[1][0]}{icon(i[1])}|  |{h[2][0]}{icon(i[2])}|  |{h[3][0]}{icon(i[3])}|  |{h[4][0]}{icon(i[4])}|    |")
      stm("|  +--+  +--+  +--+  +--+  +--+    |")
      stm("××××××××××××××××××××××××××××××××××××")

# check if player or AI has a winning hand
def is_winner(hand:list):
   rank_list=[]
   for card in hand:
      rank_list.append(card[0])
   
   counts=[]
   for i in 'AK47':
      count=rank_list.count(str(i))
      counts.append(count)
   
   if 0 not in counts:
      return True

def who_goes_first():
   if random.randint(0,1)==1:
      return 'Computer'
   else:
      return 'You'
      
def play_again():
   print("do you want to play again?.. yes?")
   ans=input().lower()
   if ans in ['yes','y']:
      return True
   else:
      return False

#picking a card::for player
def pick_a_card(dropped_cards, pack, player_hand):
   
   drawings=Drawings()
   last_dropped=dropped_cards[-1]
   
   if last_dropped[0] in ["A","K","4","7"]:
      slow_type(f"what will it be hombre.. \n1:the dropped {last_dropped} or \n2:new card from pack ")
      drawings.draw_table(last_dropped)
      
      ans=''
      options=[1,2]
      while ans not in options :
         slow_type("type 1 or 2 and press Enter..")
         ans=int(input())
         
      if int(ans)==1:
         player_hand.append(last_dropped)
         dropped_cards.remove(last_dropped)
         return player_hand
      else:
         new_card=random.choice(pack)
         player_hand.append(new_card)
         pack.remove(new_card)
         return player_hand
          
   else:
      drawings.draw_table(last_dropped)
      slow_type(f"Your turn \npress Enter to pick a card from the deck")
      
      while input() != "":
         slow_type("press Enter!!!!")
      
      new_card=random.choice(pack)
      player_hand.append(new_card)
      pack.remove(new_card)
      return player_hand
#for player      
def drop_a_card(dropped_cards,player_hand):
   options=[1,2,3,4,5]
   slow_type("here are your cards now..")
   drawings=Drawings()
   drawings.draw_drop_options(player_hand)
   
   ans=int
   while ans not in options:
      slow_type("drop a card..choose between 1-5..")
      x=input("ans:")
      ans=ans(x)
      
   slow_type("ookaaay..")
   if ans==1:
      dropped_cards.append(player_hand[0])
      player_hand.remove(player_hand[0])
      drawings.draw_hand(player_hand)
      return player_hand
   
   elif ans==2:
      dropped_cards.append(player_hand[1])
      player_hand.remove(player_hand[1])
      drawings.draw_hand(player_hand)
      return player_hand
   
   elif ans==3:
      dropped_cards.append(player_hand[2])
      player_hand.remove(player_hand[2])
      drawings.draw_hand(player_hand)
      return player_hand
   
   elif ans==4:
      dropped_cards.append(player_hand[3])
      player_hand.remove(player_hand[3])
      drawings.draw_hand(player_hand)
      return player_hand
   
   else:
      dropped_cards.append(player_hand[4])
      player_hand.remove(player_hand[4])
      drawings.draw_hand(player_hand)
      return player_hand
      
      
def ai_picks_card(dropped_cards, pack, computer_hand):
   """
   step 1:
   the AI checks if the dropped card is one of the winning
   cards,then it checks if it already has a similar card, 
   i.e:if the dropped card is 'K' but it already has a 'K'.
   if True, it ignores the dropped card and picks one from
   the deck/pack.Else, picks the dropped one
   """
   dropped_card=dropped_cards[-1]
   comp_ranks=[]
   
   for i in computer_hand:
      comp_ranks.append(i[0])
   
   if dropped_card[0] in ["A","K","4","7"]:
      slow_type("okay.. i see.. temptations..")
      
      if dropped_card[0] in comp_ranks:
         time.sleep(0.5)
         slow_type("dont need it though")
         slow_type("Let me take my chances with the deck")
         
         new_card=random.choice(pack)
         computer_hand.append(new_card)
         pack.remove(new_card)
         
         return computer_hand
         
      else:
         time.sleep(2)
         slow_type(f"aaaah! couldn't resist \ni'll take the {dropped_card}")
         computer_hand.append(dropped_card)
         dropped_cards.remove(dropped_card)
         
         return computer_hand
         
   else:
      slow_type("mmmh...")
      time.sleep(1)
      print()
      new_card=random.choice(pack)
      computer_hand.append(new_card)
      pack.remove(new_card)
      slow_type("haya!! nimepick.. cheza..")
      
      return computer_hand
      
def ai_drops_card(dropped_cards,computer_hand):
   """
   1st check for useless cards and put them in a list and if you find valuable cards put them in the 'others' list.
   the while loop checks if the 'useless' list has anything and then chooses one to drop
   the 'others' list come into play when all cards are valuable cards and thus being 5, there will be recurring cards.
   the else part of the while loop finds one of the recurring cards and drops it
   """
   useless_cards=[]
   others=[]
   for i in computer_hand:
      if i[0] not in "AK47":
         useless_cards.append(i)
      else:
         others.append(i)
         
   while len(useless_cards)>0:
      to_drop=random.choice(useless_cards)
      dropped_cards.append(to_drop)
      computer_hand.remove(to_drop)
      return computer_hand
      
   else:
      ranks=[]
      for i in others:
         ranks.append(i[0])
         
      for card in ranks:
         if ranks.count(card)>1:
            index=ranks.index(card)
            #print("computer_hand ", index)
            to_drop=computer_hand[index]
            dropped_cards.append(to_drop)
            computer_hand.remove(to_drop)
            return computer_hand
            
"""
THE GAME:
"""
def gameplay():
   while True:
      #initializes the Deck and Drawings classes
      d=Deck()
      drawings=Drawings()
      #begin
      game='AK47'
      print(game.center(57,"+"))
      slow_type(f"lets begin.")
      
      pack=d.stack()
      dropped_cards=[]
      player_hand=d.deal_cards(4,pack)
      computer_hand=d.deal_cards(4,pack)
      print()
      
      slow_type("here are your cards:")
      time.sleep(0.5)
      drawings.draw_hand(player_hand)
      
      turn=who_goes_first()
      slow_type(f"{turn} will go first")
      gameisplaying=True
      
      while gameisplaying:
         if turn=='You':
            border="Your Turn"
            print(border.center(57,"="))
            #this if for when the game has just started so there arent any dropped_cards
            if len(dropped_cards)>0:
               player_hand=pick_a_card(dropped_cards,pack,player_hand)
               player_hand=drop_a_card(dropped_cards,player_hand)
            else:
               slow_type("you pick the first card")
               time.sleep(1.5)
               new_card=random.choice(pack)
               player_hand.append(new_card)
               pack.remove(new_card)
               player_hand=drop_a_card(dropped_cards,player_hand)
               
            if is_winner(player_hand):
               drawings.draw_hand(player_hand)
               slow_type("YOU'VE WON!!!! CONGRATS")
               gameisplaying=False
               
            else:
               turn='Computer'
               
         
         else:
            border='Computer\'s turn'
            print(border.center(57,"=")) 
            if len(dropped_cards)>0:
               computer_hand=ai_picks_card(dropped_cards,pack,computer_hand)
               computer_hand=ai_drops_card(dropped_cards,computer_hand)
            else:
               new_card=random.choice(pack)
               computer_hand.append(new_card)
               pack.remove(new_card)
               computer_hand=ai_drops_card(dropped_cards,computer_hand)
               slow_type("oya!! nishacheza..")
               print()
               
            if is_winner(computer_hand):
               drawings.draw_hand(computer_hand)
               slow_type("I WIN!! HAHAHA!!! IN YOUR FACE!!")
               gameisplaying=False
               
            else:
               turn='You'
               
      
      if not play_again():
         break