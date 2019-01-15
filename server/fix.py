import os , re

path = os.getcwd()
print("Currently in ",path)

print("Contents : ")
for f in os.listdir(path):
	if re.search("0x*",f)
		print(f)
