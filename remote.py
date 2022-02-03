import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    # client runs on remote host
    sock.connect("/home/blk/remote.sock")
except Exception as e:
    print(e)
    sys.exit(1)

if __name__ == "__main__":
    data = sys.argv[1]
    sock.sendall(str.encode(data))
