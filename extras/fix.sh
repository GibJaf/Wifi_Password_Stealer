#!/bin/bash

# Delete files received from clients in current directory
for f in  ~/EH/Projects/WPA2_PSK_Stealer/From_Scratch/server/0x*;
do
	[ -e "$f" ] && rm "$f" || echo "No files from clients !"
	break
done

# Delete file generated if client runs on this machine in client folder
#if [ -e ../client/0x* ]
#then
#	rm ../client/0x*
#fi
