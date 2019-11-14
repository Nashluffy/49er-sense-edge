import mysql.connector
from gpiozero import LED

def printUpdate(SensorName):
    print('We are checking & updating the {}'.format(SensorName))

def handleGPIO(SensorName, SensorState, Pin):
    led = LED(Pin)
    led.on()

cnx = mysql.connector.connect(user='Nash', password='coolclide', database='SecurityApplication')
cursor = cnx.cursor()

query = ('SELECT * FROM SecurityTrippable')

cursor.execute(query)

for (SensorName, SensorState, SensorTripped) in cursor:
      print('The {} is currently {}. Has it been tripped? {}'.format(
              SensorName, SensorState, SensorTripped))
      if(SensorName == 'Locks'):
          #Manage GPIO 1
          printUpdate('Locks')

      elif(SensorName == 'HouseSystem'):
          #Manage GPIO 2
          printUpdate('HouseSystem')
      elif(SensorName == 'GarageDoors'):
          #Manage GPIO 3
          printUpdate('GarageDoors')
      elif(SensorName == 'Lights'):
          #Manage GPIO 4
          printUpdate('Lights')
      elif(SensorName == 'Sensors'):
          #Manage GPIO 5
          printUpdate('Sensors')
      elif(SensorName == 'Windows'):
          #Manage GPIO 6
          printUpdate('Windows')


cursor.close()
cnx.close()
