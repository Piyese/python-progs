##slot machine 2

import random
import time

class Slots:
   
   def __init__(self):
      self.icons=["★","A","K","Q","J","10","8"] 
      self.price=10
      self.offeredStake=random.randrange(200,700)
   
   def play(self):
      
      #methods
      def spinWheel():
         value=random.choice(self.icons)
         return value
      # spinWheel=lambda:random.choice(self.icons)
      
      def winnings(i):
         #full suites
         if (i[0]==i[1]==i[2] and i[1]=="★"):
            win=100000
            print("WÏÎĪLD CÂÄÅRD!!!!")
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="A"):
            win=50000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="K"):
            win=35000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="Q"):
            win=30000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="J"):
            win=20000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="10"):
            win=12000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         
         elif (i[0]==i[1]==i[2] and i[1]=="8"):
            win=10000
            print("You have won ${}".format(win))
            self.offeredStake+=win
         #2 suites
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="★"):
            win=5000
            self.offeredStake+=win
            print("you have won {}".format(win))
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="A"):
            win=5000*0.8
            self.offeredStake+=win
            print("you have won {}".format(win))
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="K"):
            win=5000*0.6
            self.offeredStake+=win
            print("you have won {}".format(win))
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="Q"):
            win=5000*0.5
            self.offeredStake+=win
            print("you have won {}".format(win))
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="J"):
            win=5000*0.4
            self.offeredStake+=win
            print("you have won {}".format(win))
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="10"):
            win=5000*0.3
            self.offeredStake+=win
            print("you have won {}".format(win))
             
  
         elif (i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2] and i[1]=="8"):
            win=5000*0.2
            self.offeredStake+=win
            print("you have won {}".format(win))
         #others
         else:
            print("not very lucky today, huh...")
  
      
      # PLAY-TIME
      print("Welcome to the Slots Bonanza.")
      print("you have ${}".format(self.offeredStake))
      print("it costs {} to play.... ready?".format(self.price))
      answer=input()
      #answer=answer.lower()
      
      #if (answer=="yes" or answer=="y"):
      if (answer.lower() in ['yes','y']):
         print("here we go......")
         print("...")
         self.offeredStake-=self.price
         #results=[self.icons[spinWheel()],self.icons[spinWheel()],self.icons[spinWheel()]]
         results=[spinWheel(),spinWheel(),spinWheel()]
         
         
         print(" «» ".join(results))
         winnings(results)
         print()
         
      else:
         print("press 'yes' or 'y'. Bye")
         
  

if __name__=="__main__":
   import doctest
   doctest.testmod()
   for i in range(10):
      Slots().play()
      
   
   
