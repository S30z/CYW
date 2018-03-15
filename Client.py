import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 8089)) 

while True:
	check = raw_input(">").upper()
	if check == 'Q':
		break
	elif check == 'R':
		s.sendall(check)
		print(s.recv(1024))
		continue
	elif check == 'S':
		message = raw_input()		
		s.send(check)
		s.send(message)
		continue
	else:
		print("\n  Please give valid input\n")
		continue 

s.close()

