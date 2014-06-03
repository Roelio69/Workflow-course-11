import re
class class2():
    def zoekOrthologen(self, userInput, userOutput):
        bestand1 = open(userInput,"r").readlines()
        bestand2 = open("LP_genes.txt", "r").readlines()
        output2 = open(userOutput+".txt","w")

        for line in bestand1:
            for line2 in bestand2:
                try:
                    if re.search(line[2:9], line2):
                        line2 = line2.split('\t')
                        line2[1] = line2[1].strip('\n')
                        output2.write(line2[0]+'\n')
                        output2.write(line2[1]+'\n')
                except:
                    print("nope")
        print("Class2 succes!")
