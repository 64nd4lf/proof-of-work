import os
import binascii
import hashlib
import sys

def main(argv):
	#target computation
	if(argv[1] == "-t"):
		#Validating arguments
		if(len(sys.argv) != 4):
			print("Error: Invalid arguments")
			exit(0)

		d = int(argv[2])
		#validating difficulty
		if(d > 256 or d < 0):
			print("Invalid difficulty, range is [0,256]")
			exit(0)
		#Caculating the target
		t = 2**(256-d)-1
		print("Target: " + "{}".format(t))
		#writing the target to a file
		f = open(argv[3], 'w')
		f.write(str(t))
		f.close()
	#Computing a solution
	elif(argv[1] == "-s"):
		if(len(sys.argv) != 5):
			print("Error: Invalid arguments")
			exit(0)
		#reading the message
		f = open(argv[2], 'r')
		m = f.read()
		f.close()
		#reading the target
		f = open(argv[3], 'r')
		t = int(f.read())
		f.close()

		flag = 1
		while(flag):
			random_num = binascii.hexlify(os.urandom(32)) # generating a random 32 bytes or 256 bit key

			hashed = hashlib.sha256(m+random_num.encode('utf-8')).hexdigest() #finding the hash of m+random_num
			if(int(hashed, 16) <= t): #checking if it a solution
				flag = 0
				f = open(argv[4], 'w') #writing the solution to a file
				f.write(random_num)
				f.close()
				print("Solution found!: " + random_num)
	#Verifying a solution
	elif(argv[1] == "-v"):
		if(len(sys.argv) != 5):
			print("Error: Invalid arguments")
			exit(0)
		#loading the message
		f = open(argv[2], 'r')
		m = f.read()
		f.close()
		#loading the target
		f = open(argv[3], 'r')
		t = int(f.read())
		f.close()
		#loading the solution
		f = open(argv[4], 'r')
		s = f.read()
		f.close()

		hashed = hashlib.sha256(m+s.encode('utf-8')).hexdigest() #computing the hash of m+s

		if(int(hashed, 16) <= t): #verifying if s is a solution
			print(1) #prints 1 if it is a solution
		else:
			print(0)

	else:
		print("Usage: pow.py <options> <arguments>")
		print("options: -t, -s, -v")

main(sys.argv)