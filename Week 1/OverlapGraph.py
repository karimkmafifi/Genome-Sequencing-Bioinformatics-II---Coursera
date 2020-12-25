def overlapGraph(patterns):
    adjLst = []
    for i in range(len(patterns)):
        lstConn = []
        for j in range(len(patterns)):
            if i != j:
                if patterns[i][1:] == patterns[j][:-1]:
                    lstConn.append(patterns[j])
        adjLst.append([patterns[i], lstConn])
    
    adjLstOut = ''
    for conn in adjLst:
        if len(conn[1]) > 0:
            adjLstOut += conn[0] + ' -> '
            for i in range(len(conn[1])):
                if i < len(conn[1])-1:
                    adjLstOut += conn[1][i] + ', '
                else:
                    adjLstOut += conn[1][i]
            adjLstOut += '\n'
    
    return adjLstOut

#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Genome Sequencing (Bioinformatics II)/Week 1/dataset_198_10.txt", "r")
#data = f.readlines()
#f.close()
#dataEdited = []
#for entry in data:
#    dataEdited.append(entry[:-1])
#returnedConnStr = overlapGraph(dataEdited)
#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Genome Sequencing (Bioinformatics II)/Week 1/overlapGraphOutput.txt", "w")
#f.write(returnedConnStr)
#f.close()