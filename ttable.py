''' an attempt at creating an exam timetable '''

import random

st1=['ABC 101','EFG 212','DKL 404','CMD 213','LED 112','KSO 310']
st2=['RYS 110','RPM 102','DKL 404','CBA 203','ROI 412','KSO 310']
st4=['RYS 110','ABC 101','EFG 212','OPQ 312','CBA 203','QTM 211']
st3=['CMD 213','ABC 101','CBA 203','OPQ 312','RPM 102','OTC 414']

all_units=[]
for i in (st1+st2+st3+st4):
   if i in all_units:
      pass
   else:
      all_units.append(i)
      
'''create a function that produces 3 units per iteration'''
def create_sessions():
   #once an exam is added to the day's session,its deprecated from all_units
   #step 1: produce three random units
   #step 2: assert that no student's exam unit appears twice
   random.shuffle(all_units)
   day_x=all_units[:3]
   print(hasattr(st3,'CMD 213'))
   print(day_x)

   
create_sessions()



while True:
   x=all_units[i]
   if x in st1:
      print('x in st1')
      break
   if x in st2:
      print('x in st2')
      break
   if x in st3:
      print('x in st4')
      break
   if x in st4:
      print('x in st4')
      break
   day_x+=x
   all_units.remove(x)
   
