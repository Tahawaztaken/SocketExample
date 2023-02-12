import socket

s = socket.socket()
port = 546
s.bind(('', port))
s.listen(5)

while True:
    print("waiting for clients")
    c,address = s.accept()
    print(f"connected to {address}")
    while True:
        message = c.recv(1024).decode()
        print(message)
        if message == "exit":
            c.close()
            break

