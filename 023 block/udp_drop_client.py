import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def client(hostname,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port))
    delay = 0.1
    text = '��ǰʱ��Ϊ�� {}'.format(datetime.now())
    data = text.encode('utf-8')
    while True:
        sock.send(data)
        sock.settimeout(delay)
        print(' {} �����������'.format(delay))
        try:
            data = sock.recv(MAX_BYTES)
            text = data.decode('utf-8')
            print('�������Ϣ�� {!r}'.format(data.decode('utf-8')))
        except socket.timeout as exc:
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('������崻�') from exc
        else:
            input('��������˳�')
            break

if __name__ == '__main__':
    client('localhost',12356)