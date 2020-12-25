import random

def eulerianCycle(graph):
    stack = []
    circuit = []
    numNonEqualDegree = 0
    nonEqualDegreeLst = []
    
    for key1 in graph:
        NumOutDegree = len(graph[key1])
        NumInDegree = 0
        for key2 in graph:
            if key1 in graph[key2]:
                NumInDegree += 1
        if NumInDegree != NumOutDegree:
            numNonEqualDegree += 1
            nonEqualDegreeLst.append([key1, NumOutDegree, NumInDegree])
    
    initVertex = ''
    if numNonEqualDegree == 2:
        if (nonEqualDegreeLst[0][1] > nonEqualDegreeLst[0][2]) and (nonEqualDegreeLst[1][2] > nonEqualDegreeLst[1][1]):
            initVertex = nonEqualDegreeLst[0][0]
        elif (nonEqualDegreeLst[0][2] > nonEqualDegreeLst[0][1]) and (nonEqualDegreeLst[1][1] > nonEqualDegreeLst[1][2]):
            initVertex = nonEqualDegreeLst[1][0]
        else:
            return circuit
    elif numNonEqualDegree == 0:
        graphKeys = graph.keys()
        initVertex = random.choice(list(graphKeys))
    else:
        return circuit 
    
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
    circuitStr = '->'.join(circuit)
    return circuitStr
            
#file = open('dataset_203_2.txt', 'r')
#data = file.readlines()
#file.close()

#dataEdited = []
#for entry in data:
#    if entry[-1:] == '\n':
#        dataEdited.append(entry[:-1])
#    else:
#        dataEdited.append(entry)
    
#graph = dict((entry.strip().split(' -> ') for entry in dataEdited))
#for key in graph:
#    graph[key] = graph[key].split(',')
    
#print(eulerianCycle(graph))