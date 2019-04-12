import socket,random, sys

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', port))
    sock.listen(3)
    print('正在监听Socket：{}', sock.getsockname())
    while True:
        sockadress, sockname = sock.accept()
        print('正在从该套接字接口处理1024字节数据：', sockname)
        n = 0
        while True:
            data = sockadress.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sockadress.sendall(output)
            n += len(data)
            print('\r  %d 已处理字节数' % (n,), end=' ')
            sys.stdout.flush()
        print()
        sockadress.close()
        print('  套接字关闭')

if __name__ == '__main__':
    server(12356)