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
    
    return preSufPatDict

def maximalNonBranchingPaths(graph, nodesInsAndOuts):
    
    contigs = []
    for node in graph:
        if nodesInsAndOuts[node] == [1, 1]:
            continue
        
        for u in graph[node]:
            contig = node
            w = u
            while True:
                contig += w[-1]
                w_degree = nodesInsAndOuts[w]
                if w_degree == [1, 1]:
                    w = graph[w][0]
                else:
                    break
            contigs.append(contig)
    
    return sorted(contigs)

def getDegrees(graph):
    degrees = {}
    for i in graph.keys():
        neighbors = graph[i]
        out_degree = len(neighbors)

        if i in degrees:
            degrees[i][1] = out_degree
        else:
            degrees[i] = [0, out_degree]

        for j in neighbors:
            if j in degrees:
                degrees[j][0] += 1
            else:
                degrees[j] = [1, 0]

    return degrees

def pathToGenome(contigs):
    finalContigs = []
    for contig in contigs:
        finalContig = ''
        for i in range(len(contig)):
            if i < len(contig)-1:
                finalContig += contig[i][0]
            else:
                finalContig += contig[i]
        finalContigs.append(finalContig)
    return ' '.join(finalContigs)

def getContigs(patterns):
    deBruijn = deBruijnGraphFromKmers(patterns)
    degrees = getDegrees(deBruijn)
    contigs = maximalNonBranchingPaths(deBruijn, degrees)
    path = pathToGenome(contigs)
    return path

#f = open("dataset_205_5.txt", "r")
#data = f.readlines()
#f.close()

#patterns = []
#for i in range(len(data)):
#    if data[i][-1:] == '\n':
#        patterns.append(data[i][:-1])
#    else:
#        patterns.append(data[i])
#contigs = getContigs(patterns)

#f = open("result.txt", "w")
#f.write(contigs)
#f.close()