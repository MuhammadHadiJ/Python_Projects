import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
server.bind(("a4:b1:c1:3a:1e:56", 4))
server.listen(1)

client, adr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('Utf-8')}")
        message = input("Enter message:")
        client.send(message.encode("Utf-8"))
except OSError as e:
    pass

client.close()
server.close()