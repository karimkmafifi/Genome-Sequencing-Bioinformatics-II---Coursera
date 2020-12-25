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
    circuitStr = '->'.join(circuit)
    return circuitStr
            
#file = open('dataset_203_6.txt', 'r')
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
    
#print(eulerianPath(graph))