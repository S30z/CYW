import socket
#first section of code to create, bind and set up socket
  s = socket.socket()
  host = socket.gethostname()
  print"socket created!"
  port =1280	
  s.bind((' ',port))
  s.listen(2)
  while True:
	c,addr = s,accept()
	inString = c.recv
	if(inString == "S")
	
	elif(inString == "R")	
	
	else
		"Error with client message"

