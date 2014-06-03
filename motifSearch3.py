import re
class class3():
    def motifSearch(self, userInput, userOutput, userOutput2, userOutput3, userOutput4):
        bestand3 = open(userInput,"r").readlines()
        bestand4 = open("WCFS1_glc_1_tss.fa").readlines()
        bestand5 = open("NC8_glc_1_tss.fa").readlines()
        bestand6 = open("WCFS1_glc_2_tss.fa").readlines()
        bestand7 = open("NC8_glc_2_tss.fa").readlines()
        output1 = open(userOutput+".txt", "w")
        output2 = open(userOutput2+".txt", "w")
        output3 = open(userOutput3+".txt", "w")
        output4 = open(userOutput4+".txt", "w")
        
        for line in bestand3:
            line = line.split("|")
            for line2 in bestand4:
                if re.search(line[1], line2):
                    output1.write(line2)
                    output1.write(bestand4[(bestand4.index(line2)+1)])
                
            for line3 in bestand5:
                if re.search(line[1], line3):
                    output2.write(line3)
                    output2.write(bestand5[(bestand5.index(line3)+1)])

            for line4 in bestand6:
                if re.search(line[1], line4):
                    output3.write(line4)
                    output3.write(bestand6[(bestand6.index(line4)+1)])

            for line5 in bestand7:
                if re.search(line[1], line5):
                    output4.write(line5)
                    output4.write(bestand7[(bestand7.index(line5)+1)])
        print("Class3 succes!")
