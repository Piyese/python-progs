''' Classic Computer Science Problems in Python'''

from functools import lru_cache,cache

#The Fibonacci Sequence
@cache
def fib(n:int)->int:
   if n<2:
      return n 
   else:
      return fib(n-2)+fib(n-1)
      
'''__________________________________________________'''      
#The Towers of Hanoi
class Stack:
   def __init__(self):
      self._container=[]
      
   def push(self,item):
      return self._container.append(item)
   
   def pop(self):
      return self._container.pop()
     
   def __repr__(self):
      return repr(self._container)
'''
num_of_discs=3
tower_A=Stack()#[1: largest ,2 ,3:smallest]
tower_B=Stack()
tower_C=Stack()
for i in range(1,num_of_discs+1):
   tower_A.push(i)
'''
   
def hanoi():
   pass

'''__________________________________________________'''



'''__________________________________________________'''

if __name__=="__main__":
   print(tower_A)