import mysql.connector

cnx = mysql.connector.connect(user='Nash', password='coolclide', database='SecurityApplication')
cursor = cnx.cursor()

query = ('SELECT * FROM SecurityTrippable')

cursor.execute(query)

for (SensorName, SensorState, SensorTripped) in cursor:
      print("The {} is currently {}. Has it been tripped? {}".format(
              SensorName, SensorState, SensorTripped))

cursor.close()
cnx.close()
