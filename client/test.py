import subprocess

#COMMAND = "ls -a"
#output = subprocess.check_output(COMMAND,shell=True)
#print (output)


dict = {'123':'abc' , '456':'def' , '789':'ghi'}
for i in dict:
	print(type(i),type(dict[i]))
