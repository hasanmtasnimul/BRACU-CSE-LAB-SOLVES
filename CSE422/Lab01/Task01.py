
if __name__ == "__main__":
    numberOfPositions = int(input())
    numberOfConnections = int(input())


    nodeDict = {}
    nodeLevelDict = {}
    visitedNodes = []

    for i in range(numberOfPositions):
        nodeDict[i] = []
        nodeLevelDict[i] = 0

    for i in range(numberOfConnections):
        nodesInput = input().split()
        nodesInput = list(map(int, nodesInput))
        node, adjacentNode = nodesInput[0], nodesInput[1]
        nodeDict[node].append(adjacentNode)
        nodeDict[adjacentNode].append(node)

    linasPosition = int(input())

    nodeQueue = []
    nodeQueue.append(0)
    visitedNodes.append(0)

    while nodeQueue:
        currentNode = nodeQueue.pop(0)
        currentNodeAdjacents = nodeDict[currentNode]
        for i in currentNodeAdjacents:
            if i not in visitedNodes:
                nodeQueue.append(i)
                nodeLevelDict[i] = nodeLevelDict[currentNode] + 1
                visitedNodes.append(i)

    print(nodeLevelDict[linasPosition])












