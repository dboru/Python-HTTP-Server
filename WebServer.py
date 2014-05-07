import socket
import sys
import threading
import time

class Server:

	def __init__(self):
		self.host = ''
		self.port = 80
		self.server = None
		self.threads = []

	def connect(self):

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.server.bind((self.host,self.port))

		except Exception as e:
			error_port = self.port
			self.port = 8080

		try:
			print ("Starting up server with host and port: ", self.port)
			self.server.bind((self.host, self.port))

		except Exception as e:
			print ("Failed to connect. Try to connect with port 8080", error_port)
			#self.server.close()

		print ("Server successfully connected socket with port: ", self.port)

		self.listen_socket()

	def listen_socket(self):

		while True:
			self.server.listen(4)

			client, addr = self.server.accept()
			print ("Got connection from: ", addr)
			c = Client(client)
			c.start()
			#self.threads.append(c)

		#for c in self.threads:
			#c.join()

class Client(threading.Thread):

	def __init__(self, client):
		threading.Thread.__init__(self)
		self.client = client

	def http_log(self, code):

		status_msg = ''
		if (code == 200):
			status_msg = 'HTTP/1.1 200 OK\n'
		elif (code == 301):
			status_msg = 'HTTP/1.1 301 Moved Permanetnly\n'
		elif (code == 400):
			status_msg = 'HTTP/1.1 400 Bad Request\n'
		elif (code == 404):
			status_msg = 'HTTP/1.1 404 Not Found\n'
		elif (code == 505):
			status_msg = 'HTTP/1.1 505 HTTP Version Not Supported\n'

		current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		status_msg += 'Date: ' + current_date + '\n'

		return status_msg


	def run(self):

		while True:

			print ("Getting data from new thread")
			request = client.recv(1024)
			string = bytes.decode(request)
			req_method = string.split(' ')[0]
			print ("Method: ", req_method)
			print ("Request body: ", string)

			if (req_method == 'GET') | (req_method == 'POST'):
				req_file = string.split(' ')
				req_file = req_file[1]

				if (req_file == '/'):
					req_file = '/index.html'
				req_file = 'webpage' + req_file
				print ("Starting up webpage: ", req_file)

				try:
					content_file = open(req_file,'rb')
					if (req_method == 'GET'):
						response_msg = content_file.read()
					content_file.close()

					print ("File requested successfully\n")
					response_status = self.http_log( 200)

				except Exception as e:
					print ("File not found 404\n", e)
					response_status = self.http_log( 404)

				response = response_status.encode()
				client.send(response)
				#self.conn.close()

			else:
				print("Unknown HTTP Request Method: ", req_method)


if __name__ == "__main__":
	s = Server()
	s.connect()







