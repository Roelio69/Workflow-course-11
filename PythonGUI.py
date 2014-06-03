# Course 11 group 3 Python 2.7 GUI program
# all used imports
from os import system
import curses
import time
from GeneFilter1 import class1
from findOrthologues2 import class2
from motifSearch3 import class3
from callMEME import class4

# returns the occured error def
def show_error(inputstring):
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "the following error has occurred: ", curses.A_BOLD)
    screen.addstr(5,4, str(inputstring))
    screen.refresh()
    time.sleep(3)

# the main code
pos = 1
x = 0
stop = 1
while stop == 1:
    screen = curses.initscr()
    curses.start_color()
    # font color, background color
    curses.init_pair(1,curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # font color, bar color
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_WHITE)
    screen.bkgd(' ', curses.color_pair(1))
    screen.keypad(1)
    # highlighted bar
    h = curses.color_pair(2)
    # normal text
    n = curses.A_NORMAL
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "Bio-Informatics Pipeline", curses.A_STANDOUT)
    screen.addstr(4,2, "Please select an option using the up and down arrow key...", curses.A_BOLD)
    
    # Detect what's highlighted by the 'pos' variable.
    if pos == 1:
        screen.addstr(5,4, "1 - Gene Finder",h)
    else:
        screen.addstr(5,4, "1 - Gene Finder",n)
    if pos == 2:
        screen.addstr(6,4, "2 - Find Orthologues",h)
    else:
        screen.addstr(6,4, "2 - Find Orthologues",n)
    if pos == 3:
        screen.addstr(7,4, "3 - Motif Search",h)
    else:
        screen.addstr(7,4, "3 - Motif Search",n)
    if pos == 4:
        screen.addstr(8,4, "4 - MEME",h)
    else:
        screen.addstr(8,4, "4 - MEME",n)
    if pos == 5:
        screen.addstr(9,4, "5 - Run all of the above", h)
    else:
        screen.addstr(9,4, "5 - Run all of the above", n)
    if pos == 6:
        screen.addstr(10,4, "6 - Exit", h)
    else:
        screen.addstr(10,4, "6 - Exit", n)
    screen.refresh()

    
    x = screen.getch()
    # variable 'x' gives pos the value of 'x', for arrow up/down system
    if x == ord('1'):
        pos = 1
    elif x == ord('2'):
        pos = 2
    elif x == ord('3'):
        pos = 3
    elif x == ord('4'):
        pos = 4
    elif x == ord('5'):
        pos = 5
    elif x == ord('6'):
        pos = 6

    # Gene Finder option (position 1)
    if pos == 1 and x == ord('\n'):
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, "This is Gene Filter")
        screen.addstr(4, 4, "Please enter a input file for Gene Filter")
        screen.addstr(9, 4, "Please name the output file for Gene Filter")
        screen.refresh()
        firstClass = class1()
        userInput = screen.getstr(6, 10, 60)
        userOutput = screen.getstr(11, 10, 60)
	try:
		firstClass.filterLPs(userInput, userOutput)
		screen.clear()
		screen.border(0)
		screen.addstr(2, 4, "Gene filter succes!")
		screen.refresh()
		time.sleep(3)
	except:
		show_error("Invalid file name. Try again.")

    # Find Orthologues option (position 2)
    if pos == 2 and x == ord('\n'):
        screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "This is Find Orthologues")
	screen.addstr(4, 4, "Please enter a input file for Find Orthologues")
	screen.addstr(9, 4, "Please name the output file for Find Orthologues")
	screen.refresh()
	secondClass = class2()
        userInput = screen.getstr(6, 10, 60)
        userOutput = screen.getstr(11, 10, 60)
	try:
		secondClass.zoekOrthologen(userInput, userOutput)
		screen.clear()
		screen.border(0)
		screen.addstr(2, 4, "Find Orthologues succes!")
		screen.refresh()
		time.sleep(3)
	except:
		show_error("Invalid file name. Try again.")					

    # Motif Search option (position 3)
    if pos == 3 and x == ord('\n'):
        screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "This is Motif Search")
	screen.addstr(4, 4, "Please enter a input file for Motif Search")
	screen.addstr(7, 4, "Please name the first output file (WCFS1_glc1)")
	screen.addstr(10, 4, "Please name the second output file (NC8_glc1)")
        screen.addstr(9, 4, "Please fill in all the parameters for MEME")
	screen.addstr(13, 4, "Please name the third output file (WCFS1_glc2)")
	screen.addstr(16, 4, "Please name the last output file (NC8_glc2)")
	screen.refresh()
	thirdClass = class3()
	userInput = screen.getstr(5, 10, 60)
	userOutput = screen.getstr(8, 10, 60)
        userOutput2 = screen.getstr(11, 10, 60)
        userOutput3 = screen.getstr(14, 10, 60)
        userOutput4 = screen.getstr(17, 10, 60)
	try:
		thirdClass.motifSearch(userInput, userOutput, userOutput2, userOutput3, userOutput4)
		screen.clear()
		screen.border(0)
		screen.addstr(2, 4, "Motif Search succes!")
		screen.refresh()
		time.sleep(3)
	except:
		show_error("Invalid file name. Try again.")
    # MEME option (position 4)
    if pos == 4 and x == ord('\n'):
        screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "This is MEME")
	screen.addstr(4, 4, "Please enter a input file for MEME")
	screen.addstr(9, 4, "Please fill in all the parameters for MEME")
	screen.addstr(10, 4, "Examples: -dna -nmotif")
	screen.refresh()
	fourthClass = class4()
	userInput = screen.getstr(6, 10, 60)
	Parameters = screen.getstr(12, 10, 60)
	try:
		fourthClass.callMEME(userInput, Parameters)
		screen.clear()
		screen.border(0)
		screen.addstr(2, 4, "MEME succes!")
		screen.refresh()
		time.sleep(3)
	except:
		show_error("Invalid file name. Try again.")
    # running all the scripts option (position 5)
    if pos == 5 and x == ord('\n'):
        screen.clear()
	screen.border(0)
        screen.addstr(2, 2, "Run all the scripts!")
        screen.addstr(4, 4, "Please enter a input file for Gene Filter")
        screen.refresh()
        firstClass = class1()
        userInput = screen.getstr(6, 10, 60)
        userOutput = "GF_output"
	try:
		firstClass.filterLPs(userInput, userOutput)
		secondClass = class2()
		userOutput2 = "FO_output"
		secondClass.zoekOrthologen(userOutput+".txt", userOutput2)
		thirdClass = class3()
		userOutput3 = "MS_output_WCFS1_glc1"
		userOutput4 = "MS_output_NC8_glc1"
		userOutput5 = "MS_output_WCFS1_glc2"
		userOutput6 = "MS_output_NC8_glc2"
		thirdClass.motifSearch(userOutput2+".txt", userOutput3, userOutput4, userOutput5, userOutput6)
		screen.clear()
		screen.border(0)
		screen.addstr(2, 4, "Run all the scripts succes!")
		screen.refresh()
		time.sleep(3)
	except:
		show_error("Invalid file name. Try again.")
    # stop program option (position 6)
    if pos == 6 and x == ord('\n'):
        stop = 0
        
    # highlight returns to the top of the list
    elif x == 258:
        if pos < 6:
            pos += 1
        else:
            pos = 1
            
    # highlight returns to the bottom of the list
    elif x == 259:
        if pos > 1:
            pos += -1
        else:
            pos = 6
            
    # error code for pushing key besides up/down arrow key
    #elif x != ord('\n'):
    #    curses.flash()
    #    show_error('Invalid Key, try the up and down arrow keys...')


curses.endwin()
system("cls")