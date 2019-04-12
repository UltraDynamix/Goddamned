import argparse, socket, sys
from datetime import datetime

MAX_BYTES = 65535

def client(host,port,bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16
    message = b'capitalize this!'

    print('发送中', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))

    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r  %d 字节的数据已发送' % (sent,), end=' ')
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('服务器返回数据接受中。。。')

    received = 0
    while True:
        data = sock.recv(1024)
        if not received:
            print('  第一份数据内容：', repr(data))
        if not data:
            break
        received += len(data)
        print('\r  %d 字节的数据已接收' % (received,), end=' ')

    print()
    sock.close()
    input('按任意键结束')

if __name__ == '__main__':
    client('localhost',12356,65535000)