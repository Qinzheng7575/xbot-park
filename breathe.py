import argparse
import socket
import datetime
import time
import struct
import multiprocessing



ttf_abs = 'C:\Windows\Fonts\STSONG.TTF'


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))

    while True:
        data, address = sock.recvfrom(1024)
        print(data)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        for i in range(6):
            sock.sendto(b'\x00', ('127.0.0.1', port))
        for i in range(2):
            sock.sendto(b'\x02', ('127.0.0.1', port))

        for i in range(6):
            sock.sendto(b'\x01', ('127.0.0.1', port))
        time.sleep(0.5)



if __name__ == "__main__":
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(
        description='send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int,
                        default=23000, help='UDP port (default 23000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
