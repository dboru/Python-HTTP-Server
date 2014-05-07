
import socket
import sys
import time

def main():
	host = ''
	port = 80

	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		socket.connect(host, port)

	except Exception as e:
		print ("Couldn't acquire port :", port,"\n")

		try:
			port = 8080
			socket.connect(host, port)

		except Exception as e:
			print ("Couldn't connect to port 80 ad 8080")

	print ("Success: client connected to host: ", host, "and port: ", port)


	while True:
		sys.stdout.write("Client ready to send request:")
		cmd = str(sys.argv)
		print ("Sending command to server: %s" % cmd)
		print ("Host name: %s" % str(sys.argv[1]))
		print ("Port: %s" % str(sys.argv[2]))
		print ("Filename: %s" % str(sys.argv[2]))
 
		socket.send(cmd)
		response = socket.recv(1024)
		if response:
			sys.stdout.write(response)
	socket.close()

if __name__ == "__main__":
	main()

