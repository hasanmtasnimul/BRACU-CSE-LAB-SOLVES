

import math
import random
import numpy as np

mutation_threshold = 0
notFoundFlag = True

def individualFitness(individual):
    n = len(individual)
    maxNonAttackingPairs = math.comb(n, 2)
    checkerBoard = np.zeros(64, dtype=int).reshape(8, 8)
    attackingPairs = 0

    #putting value 1 where it has queen in checkerboard Matrix
    for i in range(n):
        checkerBoard[-(individual[i])][i] = 1

    for i in range(n):
        queenPosition = -individual[i]

        # horizontal checking
        horizontalQueens = np.count_nonzero(checkerBoard[i, :] == 1)
        attackingPairs += math.comb(horizontalQueens, 2)

        # diagonal checking - left to right
        leftToRightDiagonal = np.diagonal(checkerBoard[queenPosition:, i:])
        leftToRightDiagonalQueens = np.count_nonzero(leftToRightDiagonal == 1)
        attackingPairs += math.comb(leftToRightDiagonalQueens, 2)

        # diagonal checking - right to left
        rightToleftReverseMatrix = (checkerBoard[:, ::-1])[-individual[-i - 1]:, i:]
        rightToleftDiagonal = np.diagonal(rightToleftReverseMatrix)
        rightToleftDiagonalQueens = np.count_nonzero(rightToleftDiagonal == 1)
        attackingPairs += math.comb(rightToleftDiagonalQueens, 2)

    return (maxNonAttackingPairs-attackingPairs)

def fitness(population, n):
    fitnessList = []
    for i in range(n):
        fitnessList.append(individualFitness(population[i]))
    return fitnessList



def select(population, popFitness):
    probList = []
    maximumFitness = math.comb(len(population[0]), 2)

    for i in popFitness:
        probList.append(i/maximumFitness)
    while(True):
        randomPosition = random.randint(0,7)
        if probList[randomPosition]>=mutation_threshold:
            return population[randomPosition]



def crossover(x, y):
    parentSize = len(x)
    randomPosition = random.randint(0, parentSize-1)
    return x[:randomPosition] + y[randomPosition:]


def mutate(child):
    childSize = len(child)
    mutatedChild = child
    randomValue = random.randint(1, childSize)
    randomPosition = random.randint(0, childSize-1)
    mutatedChild[randomPosition] = randomValue
    return mutatedChild


def GA(population, fitness):
    newPopulation = []
    for i in range(len(population)):
        x = select(population, fitness)
        y = select(population, fitness)
        child = crossover(x,y)
        #print(newPopulation)
        if random.random() <= mutation_threshold:
            child = mutate(child)
        newPopulation.append(child)
        if individualFitness(child)==28:
            notFoundFlag = False
            print(child)
            return child
    return newPopulation


if __name__ == "__main__":
    size = 8
    start_population = 10
    mutation_threshold = 0.5
    population = np.random.randint(1, size, (start_population, size))
    gen = 1
    population=population.tolist()
    popFitness = fitness(population, size)
    #print(population)
    try:
        while notFoundFlag:
            print("gen:", gen)
            gen += 1
            population = GA(population, fitness(population, size))
    except:
        pass



