import random
import random
from cards import Deck


class War:
   def __init__(self):
      self.pack=Deck.suits()
      self.pack1=[]
      self.pack2=[]
      self.stack=[]
      
   def sep_cards(self):
      self.pack1=Deck.deal_cards(26)
      self.pack2=[]
      for i in range(26):
         self.pack2.append(random.choice(self.pack))
   #will tey again later
   """
   def game_logic(self):
      while (self.stack[-1]!=self.stack[-2]):
         for i in range(10):
            drop=random.choice(self.pack1)
            self.stack.append(drop)
            self.pack1.remove(drop)
            
            drop2=random.choice(self.pack2)
            self.stack.append(drop2)
            self.pack2.remove(drop2)
            
            print(self.stack)
         
         
         
         if drop[0]==drop2[0]:
            print(drop,drop2)
            return True
         else:
            print(drop,drop2)
            print("nah")
        
      
   
s=War()
s.sep_cards()
s.game_logic()
   """