import os
import subprocess

class class4():
    def callMEME(self, userInput, Parameters):

	path = os.path.realpath(__file__)

	outputList = ["callMEME.py", userInput]

	path = path.replace(outputList[0], outputList[1])
	
	command = "cd /sharing/students/MEME/bin/ ; ./meme "+path+" -dna -nmotifs 3 -minw 20 -maxw 50 -mod zoops -minsites 150 -maxsites 745"
	subprocess.call(command, shell=True)

	commandCopy = "cp -r /sharing/students/MEME/bin/meme_out "+path.replace(outputList[1],"")	
	subprocess.call(commandCopy, shell=True)
	
	os.rename("meme_out", "output"+"("+outputList[1]+")")
