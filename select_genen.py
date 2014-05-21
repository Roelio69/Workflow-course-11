import re
def filterLPs():
    bestand = open("LP_DEG_glc.txt", "r")
    output = open("LP_DEG_glc_filtered.txt","w")

    for line in bestand:
        splitline = line.split("\t")

        if float(splitline[1]) > float(-1.0) and float(splitline[1]) < float(1.0):
            splitline[2] = splitline[2].strip('\n')
            output.write("%s\n" % splitline)
            #print(splitline)

    bestand.close()
    output.close()


def zoekOrthologen():
    bestand1 = open("LP_DEG_glc_filtered.txt","r").readlines()
    bestand2 = open("LP_genes.txt", "r").readlines()
    output2 = open("LP_genes_orthgenes.txt","w")

    for line in bestand1:
        for line2 in bestand2:
            try:
                if re.search(line[2:9], line2):
                    line2 = line2.split('\t')
                    line2[1] = line2[1].strip('\n')
                    output2.write(line2[0]+'\n')
                    output2.write(line2[1]+'\n')
                    #print(line[2:9])
                    #print(line2)
            except:
                print("nope")

def motifZoeken():
    bestand3 = open("LP_genes_orthgenes.txt","r").readlines()
    bestand4 = open("WCFS1_glc_1_tss.fa").readlines()
    bestand5 = open("NC8_glc_1_tss.fa").readlines()
    bestand6 = open("WCFS1_glc_2_tss.fa").readlines()
    bestand7 = open("NC8_glc_2_tss.fa").readlines()
    output1 = open("WCFS1_glc_1_found.txt", "w")
    output2 = open("NC8_glc_1_found.txt", "w")
    output3 = open("WCFS1_glc_2_found.txt", "w")
    output4 = open("NC8_glc_2_found.txt", "w")
    
    for line in bestand3:
        line = line.split("|")
        for line2 in bestand4:
            if re.search(line[1], line2):
                print (line2)
 #               output1.write(line2)
            
 #       for line3 in bestand5:
 #           if line[1] in line3:
 #               print (line3)
 #               output2.write(line3)

 #       for line4 in bestand6:
 #           if line[1] in line4:
 #               print (line4)
 #               output3.write(line4)

 #       for line5 in bestand7:
 #           if line[1] in line5:
 #                print (line5)
 #                output4.write(line5)

        
       
#filterLPs()
#zoekOrthologen()
motifZoeken()
