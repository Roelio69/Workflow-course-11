# calls and runs MEME (motif search) from terminal to your five-character HANaccount
import os
import subprocess

class class4():
    def callMEME(self, userInput, Path, Parameters):

	path = os.path.realpath(__file__)

	outputList = ["callMEME.py", userInput]

	path = path.replace(outputList[0], outputList[1])

	if Path.lower() == "default":
		Path = "/sharing/students/MEME/bin/"
	
	command = "cd "+Path+" ; ./meme "+path+" "+Parameters+" "
	subprocess.call(command, shell=True)

	commandCopy = "cp -r "+Path+"meme_out "+path.replace(outputList[1],"")	
	subprocess.call(commandCopy, shell=True)
	
	os.rename("meme_out", "output"+"("+outputList[1]+")")

# /sharing/students/MEME/bin/
