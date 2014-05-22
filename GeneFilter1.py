class class1():
    def filterLPs(self, userInput):
        bestand = open(userInput, "r")
        output = open("LP_DEG_glc_filtered.txt","w")
        next(bestand)
        next(bestand)
        for line in bestand:
            splitline = line.split("\t")
            if float(splitline[1]) > float(-1.0) and float(splitline[1]) < float(1.0):
                splitline[2] = splitline[2].strip('\n')
                output.write("%s\n" % splitline)

        print("Class1 succes!")
        bestand.close()
        output.close()
