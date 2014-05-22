#roept verschillende scripts aan en geeft output door.

from GeneFilter1 import class1
from findOrthologues2 import class2
from motifSearch3 import class3
#reload(GeneFilter1)
#reload(findOrthologues2)
#reload(motifSearch3)

def main():
        firstClass = class1()
        userInput = raw_input("Define gene file here: ")
        firstClass.filterLPs(userInput)
        secondClass = class2()
        secondClass.zoekOrthologen()
        thirdClass = class3()
        thirdClass.motifSearch()
        
main()
