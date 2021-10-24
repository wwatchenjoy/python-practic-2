import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_msg = input("Ответить: ")

    client.sendto(send_msg.encode('utf-8'), ('localhost', 9090))
    if send_msg == 'exit!':
        break
    elif send_msg == 'login!':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        f = open('log.txt', 'a')
        f.write(login + ' ')
        f.write(password + '\n')
        f.close()
        send_msg = "Привет! Меня зовут " + login
        client.sendto(send_msg.encode('utf-8'), ('localhost', 9090))


    back_msg = client.recv(1024).decode('utf-8')

    print('server msg: ', back_msg)
client.close()
