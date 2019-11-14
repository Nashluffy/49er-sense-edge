import socket
from gpiozero import LED
from time import sleep

led = LED(17)

port = 12345
try:
    s = socket.socket()          
    print 'Socket successfully created!'
except:
    print 'Socket creation failed'

try:
    s.bind(('', port))         
    print 'Socket binded to %s' %(port)
except:
    print 'Failed to bind to port! Is something already listening?'
        
#Socket needs to listen now
s.listen(5)      
print 'Socket is listening'     

while True:                 
    # Establish connection with client. 
    c, addr = s.accept()      
    print 'Got connection from', addr                     
    # send a thank you message to the client.  
    command = c.recv(1024)
    if command == 'TurnOn':
        print 'Turning LED on!'
        led.on()
        sleep(10)
        led.off()
        print 'Turning LED off!'
    c.send('Thank you for connecting')                              
    # Close the connection with the client 
    c.close() 

