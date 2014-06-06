Thank you for using our GitHub project!

We recommend you to install this directory somewhere on your computer, where you can easily access it from the terminal (so don't have directory names with spaces in it or you clone the directory into the temp. folder).
To start up the program, type in "python PythonGUI.py" in your terminal in your cloned github folder (Workflow-course-11).
By activating the GUI, you can now select any of the options and run any script that's included in the directory. 


The GUI consists of the following modules: 
Gene Finder -> reads a text file with numeric values in columns from L.PLantarum. The script reads only the second column and filters it (filters numeric values between -1 and 1), the first column defines (name) the numeric value in the second column. After filtering the numeric values between -1 and 1, plus name, is placed in the output file in a list format. 
Start the module and the first thing you type in is the input file (include the format with it, for example "input.txt") and press enter. finally fill in the name for your output file (don't include the format in the name, it does it automatically). If everything went well, you'll see succes written in the terminal. 

Find Orthologues -> reads a file with numeric values in list format from L.PLantarum (output of Gene Finder). The first column, where the name is defined for the numeric value in the second column, is used for searching the same one in LP_genes and writes both names into the output file. 
Start the module and the first thing you type in is the input file (include the format with it, for example "input.txt") and press enter. finally fill in the name for your output file (don't include the format in the name, it does it automatically). If everything went well, you'll see succes written in the terminal.

Motif Search -> reads a file with names, preferably gene orthologues from L.PLantarum (output of Find Orthologues). The names in the file are used for searching the same name in the fasta files. When the name is found in the fasta files, the name plus the sequence from the fasta file will be written in the output file. 
Start the module and the first thing you type in is the input file (include the format with it, for example "input.txt") and press enter. finally fill in the names for your four output files (don't include the format in the name, it does it automatically). If everything went well, you'll see succes written in the terminal.

MEME -> you have to install the MEME program before you can run this module. You have to download MEME first from this website (http://ebi.edu.au/ftp/software/MEME/index.html) (tip: download the pre-patched version, so you don't have to update MEME after you've installed it). Then via terminal commands (use linux terminal or cygwin terminal, not the windows terminal) configure MEME in the directory where it is located (install guide MEME: http://meme.nbcr.net/meme/doc/meme-install.html). After installation and configuration of MEME, you can now use this module. 
Start the module and the first thing you type in is the input file (include the format with it, for example "input.txt") and press enter. Then fill in the path, where MEME is installed (include "/" before and after the path), and press enter. Finally fill in the name for your output file (don't include the format in the name, it does it automatically). if everything went correctly, you will now see the MEME program running in the terminal. If not, please try again and read carefully the instructions. 

Run all of the above -> (install MEME to use this option) automatically runs the four modules (Gene Finder, Find Orthologues, Motif Search and MEME) and put all the results in the directory where all the scripts are. 
Start the module and the first thing you type in is the input file (include the format with it, for example "input.txt") and press enter. Finally fill in the path, where MEME is installed (include "/" before and after the path) and press enter. The terminal shows a percentage of how much is completed from this module. When it shows succes, the module is done and all the results are in the directory where all the scripts are. 

Script selection -> (install MEME to use this option) runs the four modules (Gene Finder, Find Orthologues, Motif Search and MEME) in your prefered way. The output will be located in the same directory as where all the scripts are. 
start the module and fill in the numbers for the scripts your want in that order (1=Gene Finder, 2=Find Orthologues, 3=Motif Finder and 4=MEME). The numbers can be repeated and have to follow eachother with a space (for example=1 3 2 2 4 1 1 2). 

See all input text files in directory -> generates a list of all the text files (.txt), without the LP_genes and readme files shown, which possibly can be used for the modules in the GUI.

Exit -> it quits the program and clears the terminal plus deletes all .pyc files (python compiled files) 