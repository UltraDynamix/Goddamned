import socket,random

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('正在监听： {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print('Pretending to drop packet from {}'.format(address))
            continue
        text = data.decode('utf-8')
        print('客户端:{} 发来消息 {!r}'.format(address, text))
        text = '数据长度为 {}'.format(len(data))
        data = text.encode('utf-8')
        sock.sendto(data, address)

if __name__ == '__main__':
    server(12356)