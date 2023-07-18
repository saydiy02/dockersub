import socket
import mysql.connector
import time

def Main():
  host = "172.18.0.4"
  port = 8667

  mydb = mysql.connector.connect(host = "172.17.0.1", port =30000, user = "saadah", password = "odah", database = "sir_db")
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM mytable")
  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    time.sleep(1)

  mySocket = socket.socket()
  mySocket.connect(("172.18.0.7",30000))

  msg = input(" - ")

  while msg != 'q':
    mySocket.send(msg.encode())
    data = mySocket.recv(1024).decode()

    print ('Received from server' + data)

    msg = input (" - ")
 
  mySocket.close()


if __name__ == '__main__':
  Main()
