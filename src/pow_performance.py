import os
import binascii
import hashlib
import sys
import timeit

def main(argv):
	if(len(sys.argv) != 3): #valudate arguments
		print("Error: Invalid arguments")
		exit(0)

	d = int(argv[1])
	if(d > 256 or d < 0): #valudate difficulty
		print("Invalid difficulty, range is [0,256]")
		exit(0)
	t = 2**(256-d) - 1 #computing the target
	print("Difficulty: " + "{}".format(d))

	#loading the message
	f = open(argv[2], 'r')
	m = f.read()
	f.close()

	start = timeit.default_timer() #starts timer
	flag = 1
	while(flag): #runs until it finds a solution
		random_num = binascii.hexlify(os.urandom(32)) # geberating a random 32 bytes or 256 bit key
		hashed = hashlib.sha256(m+random_num.encode('utf-8')).hexdigest()
		if(int(hashed, 16) <= t):
			flag = 0
			print("Solution found!: " + random_num)
	stop = timeit.default_timer() #timer stops
	print("Time: " + "{}".format(stop - start)) #computing run time and printing
	print("---------------------------------------")

main(sys.argv)