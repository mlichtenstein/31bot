
#can Max write a service?  Let's find out!

#this is meant to be run with python 2

print("beginning test client!  Importing sys...")
import sys

print("type in letters and I will modify them")
f = open("test_service.log","w+")
while True:
	line = sys.stdin.readline()
	if line:
		f.write(line)
		output = ""
		for char in line:
			output = output + chr(ord(char)+32)
		sys.stdout.write(output)
		f.write(output)
