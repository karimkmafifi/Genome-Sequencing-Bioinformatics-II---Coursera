import random

def eulerianPath(graph, k):
    stack = []
    circuit = []
    initVertex = ''
    initVertex = random.choice(list(graph.keys()))
        
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
    circuit = circuit[:-k+1]
    #circuitStr = '->'.join(circuit)
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
    path = eulerianPath(deBruijn, k)
    text = pathToGenome(path)
    return text

#k = 9
#patterns = ["".join(seq) for seq in itertools.product("01", repeat=k)]
#print(stringReconstruction(k, patterns))