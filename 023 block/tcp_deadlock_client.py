import argparse, socket, sys
from datetime import datetime

MAX_BYTES = 65535

def client(host,port,bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16
    message = b'capitalize this!'

    print('������', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))

    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r  %d �ֽڵ������ѷ���' % (sent,), end=' ')
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('�������������ݽ����С�����')

    received = 0
    while True:
        data = sock.recv(1024)
        if not received:
            print('  ��һ���������ݣ�', repr(data))
        if not data:
            break
        received += len(data)
        print('\r  %d �ֽڵ������ѽ���' % (received,), end=' ')

    print()
    sock.close()
    input('�����������')

if __name__ == '__main__':
    client('localhost',12356,65535000)