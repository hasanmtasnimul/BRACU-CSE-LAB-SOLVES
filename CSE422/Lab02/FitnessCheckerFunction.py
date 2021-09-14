import math
import numpy as np

x = [6, 3, 1, 8, 5, 2, 4, 7]

checkerBoard = np.zeros(64, dtype=int).reshape(8,8)
attackingPairs = 0

for i in range(8):
    checkerBoard[-(x[i])][i] = 1
#print(checkerBoard)

for i in range(8):
    queenPosition = -x[i]

    #horizontal checking
    horizontalQueens = np.count_nonzero(checkerBoard[i, :]==1)
    attackingPairs += math.comb(horizontalQueens, 2)

    #diagonal checking - left to right
    leftToRightDiagonal = np.diagonal(checkerBoard[queenPosition:, i:])
    leftToRightDiagonalQueens = np.count_nonzero(leftToRightDiagonal==1)
    attackingPairs += math.comb(leftToRightDiagonalQueens, 2)

    # diagonal checking - right to left
    rightToleftReverseMatrix = (checkerBoard[:, ::-1])[-x[-i-1]:, i:]
    rightToleftDiagonal = np.diagonal(rightToleftReverseMatrix)
    rightToleftDiagonalQueens = np.count_nonzero(rightToleftDiagonal==1)
    attackingPairs += math.comb(rightToleftDiagonalQueens, 2)



print(checkerBoard)