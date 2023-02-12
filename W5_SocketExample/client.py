import socket



s = socket.socket()
port = 546
s.connect(('127.0.0.1', port))

while True:
    command = input("what you want to do?>> ")
    s.send(command.encode())

    if command=="exit":
       s.close()
       break