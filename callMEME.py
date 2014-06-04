# calls and runs MEME (motif search) from terminal to your five-character HANaccount
import os
from os import system
import subprocess

class class4():
    def callMEME(self, userInput, MEMEpath, Parameters):

	path = os.path.realpath(__file__)

	outputList = ["callMEME.py", userInput]

	path = path.replace(outputList[0], outputList[1])

	command = "cd "+MEMEpath+" ; ./meme "+path+" "+Parameters
	subprocess.call(command, shell=True)

	commandCopy = "mv -f "+MEMEpath+"meme_out "+path.replace(outputList[1],"")	
	subprocess.call(commandCopy, shell=True)
	
        os.rename("meme_out", "output"+"("+outputList[1]+")")

# /sharing/students/MEME/bin/
