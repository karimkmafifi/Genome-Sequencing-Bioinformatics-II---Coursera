def deBruijnGraphFromKmers(patterns):
    preSufPat = []
    for ptt in patterns:
        preSufPat.append(ptt[:-1])
        preSufPat.append(ptt[1:])
    preSufPat = list(set(preSufPat))   
    preSufPatDict = dict((el, []) for el in preSufPat)
    
    for ptt in patterns:
        prefix = ptt[:-1]
        suffix = ptt[1:]      
        preSufPatDict[prefix].append(suffix)
    
    connsLstOut = ''
    for key in preSufPatDict:      
        if len(preSufPatDict[key]) > 0:
            connsLstOut += key + ' -> '
            for i in range(len(preSufPatDict[key])):
                if i < len(preSufPatDict[key])-1:
                    connsLstOut += preSufPatDict[key][i] + ', '
                else:
                    connsLstOut += preSufPatDict[key][i]
            connsLstOut += '\n'
    
    return connsLstOut

#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Genome Sequencing (Bioinformatics II)/Week 1/dataset_200_8.txt", "r")
#data = f.readlines()
#f.close()
#dataEdited = []
#for entry in data:
#    dataEdited.append(entry[:-1])
#returnedConnStr = deBruijnGraphFromKmers(dataEdited)
#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Genome Sequencing (Bioinformatics II)/Week 1/deBruijnGraphFromKmersOutput.txt", "w")
#f.write(returnedConnStr)
#f.close()