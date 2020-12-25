import random

def eulerianPath(graph):
    
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
    #circuitStr = '->'.join(circuit)
    #return circuitStr
    return circuit

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

def pathToGenome(path):
    genome = ''
    for i in range(len(path)):
        if i < len(path)-1:
            genome += path[i][0]
        else:
            genome += path[i]
    return genome

def stringReconstruction(k, patterns):
    deBruijn = deBruijnGraphFromKmers(patterns)
    path = eulerianPath(deBruijn)
    text = pathToGenome(path)
    return text

f = open("input.txt", "r")
data = f.readlines()
f.close()
k = 0
patterns = []
for i in range(len(data)):
    if i == 0:
        if data[0][-1:] == '\n':
            k = int(data[0][:-1])
        else:
            k = int(data[0])
    else:
        if data[i][-1:] == '\n':
            patterns.append(data[i][:-1])
        else:
            patterns.append(data[i])
returnedConnStr = stringReconstruction(k, patterns)
print(returnedConnStr)