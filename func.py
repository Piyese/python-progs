import sys,time,random

#random functions and classes for imports

#1. JSONField field default fill for the rpg-API project
def getmod(model):
   mappings={
      "biz_and_prop":dict(quantity=0,cost=0,income=0),
      "armoury":dict(quantity=0,attack=0,defence=0),
      "vehicles":dict(quantity=0,attack=0,defence=0),
      "mobs":dict(capacity=dict(weapons=10, vehicles=0),level=0,points=0, quantity=0),
      "supportmobs":dict(level=0,points=0,active=False)
   }
   
   try:
      return mappings[model]
   except KeyError:
      return 'not in the options, check the applicable *args'
#2.dramatic print outs.. mostly for games
def slow_type(t:str):
   typing_speed=100#wpm
   for letter in t:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(random.random()*10/typing_speed)
   print()
# a little less dramatic
def slow_type_mod(t:str):
   for letter in t:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.01)
   print()

#. custom datatype
class FuzzyBool:
   """
   A Boolean variation:
   We will use floating-point values with 0.0 denoting False and 1.0 denoting True.
   In this system, 0.5 means 50 percent true, and 0.25 means 25 percent true, and so on
   """
   def __init__(self,value):
      self.__value=value if 0.0<=value<=1.0 else 0.0
      #value attribute private because we want FuzzyBool to behave like immutables, so allowing access to the attribute would be wrong
   
   def __invert__(self):
      return FuzzyBool(1.0 - self.__value)
   pass   
   #to be continued
class Bin:
   key="nRaifdjFkhjqSZbrKxZ4JVFmM4DDWKyAaCgDMKXEEGWLvPysSNqsVKM7Nu2rVXpc"
   secret_key="z1IbeuGNYQqMuA4TRtsiD4uucAc7UNjw3Qkel057JlKMWEqwh6X2qAZzRna3dZSY"
   pass