import socket
from threading import *

class DataMd:

	def __init__(self, key, host, port):
		self.key = key
		self.host = host
		self.port = port


	def send(self, pointA, pointB):
		fromData = pointA.getData()
		toData = pointB.getData()
		data = '{ "key": "'+ self.key +'", "from": '+ fromData +', "to": '+ toData +' }'

		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		clientsocket.connect((self.host, self.port))
		
		Client(clientsocket, 'hi'.encode('utf-8'))


class Point:

	def __init__(self, name, color='#000000'):
		self.name = name
		self.color = color

	def getData(self):
		return '{ name: "'+self.name+'", color: "'+self.color+'" }'



class Client(Thread):
    def __init__(self, socket, data):
        Thread.__init__(self)
        self.sock = socket
        self.data = data
        self.start()

    def run(self):
        self.sock.send(self.data)
        self.sock.close()

