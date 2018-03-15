import socket
#first section of code to create, bind and set up socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
print"socket created!"
#s1=socket.gethostname
port =8089	
s.bind(("localhost",port))
s.listen(2)
chatLog = ''
while True:
	c,addr = s.accept()
	inString = c.recv
	#client is sending a message,recving 1 message to add to the string
	if inString == "S":
		print "were here S"
		inMessage = c.recv
		chatLog= chatLog+inMessage+"\n"

	#client is reciving an update from the sever
	elif inString == "R":
		print "were here R"	
		c.send(chatLog)
	else:
		"Error with client message"
	
