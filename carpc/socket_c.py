import socket

client_socket = socket.socket()
#address = '192.169.100.102'
address = '192.169.100.127'
port = 8010
client_socket.connect((address,port))

while True:
    try:
        data = soc.recv(1024)
        print("Server>",data)
    except:
        pass
    finally:
        break
