import random

def eulerianPath(graph, k):
    
    stack = []
    circuit = []
    initVertex = ''
    endVertex = ''
    allNodesUnique = []
    
    for key1 in graph:
        allNodesUnique.append(key1)
        for key2 in graph[key1]:
            allNodesUnique.append(key2)
            
    allNodesUnique = list(set(allNodesUnique))
    nodesInsAndOuts = {}
    
    for val in allNodesUnique:
        nodesInsAndOuts[val] = []
    
    for key in nodesInsAndOuts:
        if key in graph:
            nodesInsAndOuts[key].append(len(graph[key]))
        else:
            nodesInsAndOuts[key].append(0)
        
        numIns = 0
        for key2 in nodesInsAndOuts:
            if key2 in graph:
                if key in graph[key2]:
                    numIns += 1
        
        nodesInsAndOuts[key].append(numIns)
    
    for key in nodesInsAndOuts:
        if nodesInsAndOuts[key][0]>nodesInsAndOuts[key][1]:
            initVertex = key
        elif nodesInsAndOuts[key][1]>nodesInsAndOuts[key][0]:
            endVertex = key
    
    if endVertex in graph:
        graph[endVertex].append(initVertex)
    else:
        graph[endVertex] = [initVertex]
        
    currVertex = initVertex
    
    while 1:
        if (len(graph[currVertex]) == 0) and (len(stack)==0):
            break
        
        if len(graph[currVertex]) == 0:
            circuit.append(currVertex)
            currVertex = stack.pop()
        else:
            stack.append(currVertex)
            neighbors = graph[currVertex]
            prvVertex = currVertex
            currVertex = random.choice(neighbors)
            graph[prvVertex].remove(currVertex)
    
    circuit.append(initVertex)
    circuit.reverse()
    circuit = circuit[:-1]
    return circuit

def deBruijnGraphFromKmersPaired(patterns):
    preSufPat = []
    for ptt in patterns:
        preSufPat.append((ptt[0][:-1], ptt[1][:-1]))
        preSufPat.append((ptt[0][1:], ptt[1][1:]))
    preSufPat = list(set(preSufPat))   
    preSufPatDict = dict((el, []) for el in preSufPat)
    
    for ptt in patterns:
        prefix = (ptt[0][:-1], ptt[1][:-1])
        suffix = (ptt[0][1:], ptt[1][1:]) 
        preSufPatDict[prefix].append(suffix)
    
    return preSufPatDict

def pathToGenomePaired(k, d, path):
    print(path)
    firstPatterns = [val[0] for val in path]
    secondPatterns = [val[1] for val in path]
    
    prefixString = [firstPatterns[i][0] for i in range(len(firstPatterns)-1)]
    suffixString = [secondPatterns[i][0] for i in range(len(secondPatterns)-1)]
    
    prefixString += firstPatterns[-1]
    suffixString += secondPatterns[-1]
    
    for i in range(k+d+1, len(prefixString)):
        if prefixString[i] != suffixString[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    
    return ''.join(prefixString+suffixString[-k-d:])

def stringReconstructionPaired(k, d, patterns):
    deBruijn = deBruijnGraphFromKmersPaired(patterns)
    path = eulerianPath(deBruijn, k)
    text = pathToGenomePaired(k, d, path)
    return text

f = open("input.txt", "r")
data = f.readlines()
f.close()
k = 0
d = 0
patterns = []
for i in range(len(data)):
    line = data[i]
    if line[-1:] == '\n':
        line = line[:-1]     
    if i == 0:
        k = int(line.split()[0])
        d = int(line.split()[1])
    else:
        patterns.append((line.split('|')[0], line.split('|')[1]))

returnedConnStr = stringReconstructionPaired(k, d, patterns)
print(returnedConnStr)