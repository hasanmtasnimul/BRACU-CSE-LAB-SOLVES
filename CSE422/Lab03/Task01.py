import random
import math

infinity = math.inf
alpha = -infinity
beta = infinity
afterPrunedVisitCount = 0
inputDepth = 0

def alphaBetaPrune(position, depth, alpha, beta, maximizingPlayer, leaves):
   global afterPrunedVisitCount
   if depth == inputDepth:
       afterPrunedVisitCount += 1
       return leaves[position]

   if maximizingPlayer:
       maxEval = -infinity
       for i in range(0, branches):
           eval = alphaBetaPrune(position * branches + i, depth + 1, alpha, beta, False, leaves)
           maxEval = max(maxEval, eval)
           alpha = max(alpha, maxEval)
           if beta <= alpha:
               break
       return maxEval

   else:
       minEval = infinity
       for i in range(0, branches):
           eval = alphaBetaPrune(position * branches + i, depth + 1, alpha, beta, True, leaves)
           minEval = min(beta, eval)
           beta = min(beta, minEval)
           if beta <= alpha:
               break
       return minEval


if __name__ == '__main__':
   #inputs

   turns = int(input())
   branches = int(input())
   rangeOfNotes = input().split()
   rangeOfNotes = list(map(int, rangeOfNotes))

   inputDepth = 2 * turns
   totalLeafNodes = branches ** inputDepth
   #leafNodeFromBux = [3, 12, 8, 2, 4, 6, 14, 5, 2]

   randomGenleaf = random.sample(range(rangeOfNotes[0], rangeOfNotes[1]), totalLeafNodes)
   maximumAmount = alphaBetaPrune(0, 0, alpha, beta, True, randomGenleaf)
   print(randomGenleaf)



   print("Depth: ", inputDepth)
   print("Branch: ", branches)
   print("Terminal States (Leaf Nodes): ", totalLeafNodes)
   print("Maximum amount: ", maximumAmount)
   print("Comparisons: ", totalLeafNodes)
   print("Comparisons: ", afterPrunedVisitCount)



