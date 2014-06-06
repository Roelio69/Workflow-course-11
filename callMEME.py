# calls and runs MEME (motif search) from terminal to your five-character HANaccount
import os
from os import system
import subprocess

class class4():
    def callMEME(self, userInput, MEMEpath, Parameters):

	path = os.path.realpath(__file__)

	outputList = ["callMEME.py", userInput]

	path = path.replace(outputList[0], outputList[1])

	command = "cd "+MEMEpath+" ; ./meme "+path+" -oc "+path.replace(outputList[1], "output")+" "+Parameters
	subprocess.call(command, shell=True)
	
        os.rename("output", "output"+"("+outputList[1]+")")
