import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_msg = input("Ты сказал: ")

    client.sendto(send_msg.encode('utf-8'), ('localhost', 9090))
    if send_msg == 'exit!':
        break

    back_msg = client.recv(1024).decode('utf-8')

    print(back_msg)
client.close()
