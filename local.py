import socket
import sys
import os
import subprocess

addr = "/home/blk/local.sock"

if __name__ == "__main__":
	try:
		os.unlink(addr)
	except Exception as e:
		print(e)
		sys.exit(1)

	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.bind(addr)
	sock.listen(1)

	while True:
		conn, client_addr = sock.accept()

		try:
			data = b''
			while True:
				buf = conn.recv(128)
				if not buf:
					break

				data += buf
		except Exception as e:
			print(e)
			sys.exit(1)

		data = data.decode("utf-8")

		print("Opening:", data)
		#os.execve("/usr/sbin/google-chrome-stable", ["google-chrome-stable", data], os.environ)
		#os.execve("/usr/sbin/xdg-open", ["local.py", data], os.environ)
		subprocess.run(["/usr/sbin/google-chrome-stable", data])
