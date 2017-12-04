#ok, so Max can write a stdin service.  Can he write a stdout client?

import subprocess
import time

print("test client start, opening subprocess:")
ps = subprocess.Popen(	["python2", "test_service.py"],
			stdin = subprocess.PIPE, 
			stdout = subprocess.PIPE, 
			stderr = subprocess.PIPE)

for i in range(65, 128):
	print("writing",chr(i),"to test_service...")
	str_to_send = chr(i)+"\n" 
	
	ps.stdin.write(str_to_send.encode("utf8"))
	#stdoutdata = ps.stdout.read()
	#stdoutdata = ps.communicate(str_to_send.encode("utf-8") )[0]
	#str_rec = stoutdata.decode("utf8")

	#print("result is",str_rec+"\n")
	time.sleep(1)
