import socket,random, sys

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', port))
    sock.listen(3)
    print('���ڼ���Socket��{}', sock.getsockname())
    while True:
        sockadress, sockname = sock.accept()
        print('���ڴӸ��׽��ֽӿڴ���1024�ֽ����ݣ�', sockname)
        n = 0
        while True:
            data = sockadress.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sockadress.sendall(output)
            n += len(data)
            print('\r  %d �Ѵ����ֽ���' % (n,), end=' ')
            sys.stdout.flush()
        print()
        sockadress.close()
        print('  �׽��ֹر�')

if __name__ == '__main__':
    server(12356)