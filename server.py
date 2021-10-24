import socket

fwq = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

fwq.bind(('localhost', 9090))

print('Начать чат! ')

while True:

    data, addr = fwq.recvfrom(1024)

    recvmsg = data.decode('utf-8')

    if recvmsg == 'exit!':
        print("Участник" + str(addr) + "добровольно закончил чат с тобой, пока!")
        continue
    elif recvmsg == 'login!':
        print("Пользователь " + str(addr) + " регистрируется")

    print(str(addr) + ' client msg: ' + recvmsg)
    replymsg = input('Ответить: ')

    fwq.sendto(replymsg.encode('utf-8'), addr)

fwq.close()
