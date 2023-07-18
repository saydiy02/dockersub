import socket
import mysql.connector

def Main():
  host = "172.18.0.7"
  port = 8667

  mySocket = socket.socket()
  mySocket.bind((host,30000))

  mySocket.listen(1)
  conn, addr = mySocket.accept()
  print ("Connection from " + str(addr))

  while True:
    data = conn.recv(1024).decode()

    if not data:
      break

    print ("From connected user: " + str(data))

    data = str(data).upper()
    print("Sending ..." + str(data))
    conn.send(data.encode())

  conn.close()


if __name__ == "__main__":
  Main()
