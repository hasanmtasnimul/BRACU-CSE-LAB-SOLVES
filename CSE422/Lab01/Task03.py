"""
the main idea here is to take
inputs in the input dictionary
in a way so that the directions
are reversed this way we can
traverse from destination to
each node and get their level
or distance. LASTLY calculate the
minimum moves among the participant
"""

def returnLevel(startNode, nodeDict):
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
    return nodeLevelDict

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
        nodeDict[adjacentNode].append(node)

    linasPosition = int(input())
    noOfparticipants = int(input())
    participantPositions = []

    for i in range(noOfparticipants):
        participantInput = int(input())
        participantPositions.append(participantInput)

    nodeDistanceDict = returnLevel(linasPosition, nodeDict)
    participantMoves = []
    for i in participantPositions:
        participantMoves.append(nodeDistanceDict[i])
    print(nodeDict)
    print(nodeDistanceDict)
    print(min(participantMoves))














