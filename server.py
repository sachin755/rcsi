#!/usr/bin/python

import socket
import subprocess
import Tkinter

s = socket.socket()
host = "127.0.0.1"

port = input("port : ")

s.bind((host,port))

top = Tkinter.Tk()

s.listen(5)

def transfer():
	from tkFileDialog import askopenfilename
	Tkinter.Tk().withdraw()
	filename = askopenfilename()
	c.send('sendack')
	if filename != '':
		f = open(filename)
	        data = f.readlines()
	        length = len(data)
        #print length
	        for i in range(0,length):
	                c.send(data[i])
	        print "transfer done"
	        c.send("()()()transfer ok")

def listen(command):
#	while True:
#		c.send(command)
#		data = c.recv(1024)
#		break
#	return data
	return ""

def execute():
	comnd = Command.get("1.0","1000.0")
	c.send(comnd)

def ls():
#	data = listen('ls')
	c.send('ls')
	print " going deeper "
#	print dir(List)
#	while True:
#		print c.recv(1024)
#		if c.recv(1024) == "end":
#			break
	av = "never back down"
		#data = c.recv(1024)
 		#print data
	Result.config(text="sachin")
	Result.update()

#	print dir(Result)
	#print c.recv(1024)
#	print data

v = "avengers"
while True:
	c, addr = s.accept()

	Transfer = Tkinter.Button(top, text ="Execute", command = execute)
	Command = Tkinter.Text(top)
	Result = Tkinter.Label(top,text = v)
	Result.pack()
	Command.pack()
	Transfer.pack()
	top.mainloop()
        while True:
	        data = c.recv(1024)
		print data
#		print "-----"
        #        break
        #return data

#	f = open('rock.mp3')
#	data = f.readlines()
#	length = len(data)
#	print length
#	for i in range(0,length):
#		c.send(data[i])
#	print "transfer done"
#	c.send("transfer ok")
	c.close()
	
s.close()

