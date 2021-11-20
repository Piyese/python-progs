""" A DECK OF CARDS """
import random

class Deck:
   
   def __init__(self):
      self.ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
      self.suits=["clubs","hearts","spades","diamonds"]
      
   def stack(self):
      pack=[]
      for i in self.ranks:
         for j in self.suits:
            pack.append([i,j])
      return pack
      
   def deal_cards(self,n:int,pack:list):
      dealt_cards=[]
      for deal in range(n):
         card=random.choice(pack)
         dealt_cards.append(card)
         pack.remove(card)
      return dealt_cards
      
      
"""
if __name__=="__main__":
   import doctest
   doctest.testmod()
""" 
 
"""   
   def new(*args):
      for x in args:
         print(x)

Deck.new("duck","goose","gander")
"""