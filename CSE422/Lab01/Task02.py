def returnLevel(startNode, destinationNode, nodeDict):
    nodeLevelDict = {}
    for i in nodeDict.keys():
        nodeLevelDict[i] = 0
    visitedNodes = []
    nodeQueue = []
    nodeQueue.append(startNode)
    visitedNodes.append(startNode)
    while nodeQueue:
        currentNode = nodeQueue.pop(0)
        currentNodeAdjacents = nodeDict[currentNode]
        for i in currentNodeAdjacents:
            if i not in visitedNodes:
                nodeQueue.append(i)
                nodeLevelDict[i] = nodeLevelDict[currentNode] + 1
                visitedNodes.append(i)
    return nodeLevelDict[destinationNode]

def winner(larasDistance, norasDistance):
    if (norasDistance == larasDistance):
        print(both)
    else:
        if norasDistance<larasDistance:
            print("Nora")
        else:
            print("Lara")

if __name__ == "__main__":
    numberOfPositions = int(input())
    numberOfConnections = int(input())

    nodeDict = {}

    for i in range(numberOfPositions):
        nodeDict[i] = []

    for i in range(numberOfConnections):
        nodesInput = input().split()
        nodesInput = list(map(int, nodesInput))
        node, adjacentNode = nodesInput[0], nodesInput[1]
        nodeDict[node].append(adjacentNode)
        nodeDict[adjacentNode].append(node)

    linasPosition = int(input())
    norasPosition = int(input())
    larasPosition = int(input())

    print(nodeDict)
    print(linasPosition)
    print(norasPosition)
    print(larasPosition)

    norasDistance = returnLevel(norasPosition, linasPosition, nodeDict)
    larasDistance = returnLevel(larasPosition, linasPosition, nodeDict)

    winner(larasDistance, norasDistance)