import socket, sys
from slots import Slots

s=socket.socket()
Slots.slow_type("socket successfully created")
sys.stdout.flush()

port=8080

s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(5)

while True:
   c, addr=s.accept()
   print(f"got connection from {addr}")
   c.send('thanks')
   c.close()