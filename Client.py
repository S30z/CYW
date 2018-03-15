import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('127.0.0.1', 8089)) 

def server_check():
	while True:
		check = input("  Would you like to (S)end or (R)eceive a message?\n  ").upper()
		if check == 'Q':
			break
		elif check == 'R':
			s.sendall(check)
			print(s.recv(1024))
			continue
		elif check == 'S':
			s.sendall(check)
			message = input()
			s.sendall(message)
			continue
		else:
			print("\n  Please give valid input\n")
			continue


server_check() 

s.close()



