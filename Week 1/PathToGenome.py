def pathToGenome(path):
    genome = ''
    for i in range(len(path)):
        if i < len(path)-1:
            genome += path[i][0]
        else:
            genome += path[i]
    return genome

#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Genome Sequencing (Bioinformatics II)/Week 1/dataset_198_3.txt", "r")
#data = f.readlines()
#f.close()
#dataEdited = []
#for entry in data:
#    dataEdited.append(entry[:-1])
#print(pathToGenome(dataEdited))