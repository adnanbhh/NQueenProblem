import numpy as np
import random

def countThreat (population):
    threat = 0

    for currentGene in range(0, len(population)):
        currentQueen = [currentGene, population[currentGene]]


        for previousGene in range (0, currentGene):
            previousQueen = [previousGene, population[previousGene]]

            slope = (currentQueen[1] - previousQueen[1]) / (currentQueen[0] - previousQueen[0])


            if slope == 0:
                threat += 1
                break


            elif slope == 1 or slope == -1:
                threat += 1
                break

    return threat


def initializePopulation (populationSize, chromosomeSize):
    population = []
    for i in range(populationSize):
        population.append(np.random.random_integers(low=0, high=chromosomeSize-1, size=(chromosomeSize)))

    return population


def sortPopulation (population):
    population.sort(key=countThreat)
    return population


def crossover(population, crossoverCount):
    chromosomeLenght = len(population[0])
    for i in range(0, crossoverCount):
        crossoverParent1 = random.choice(population)
        crossoverParent2 = random.choice(population)

        crossoverPoint = random.randint(1, chromosomeLenght-1)

        child1 = []
        child1.extend(crossoverParent1[:crossoverPoint])
        child1.extend(crossoverParent2[crossoverPoint:])
        child2 = []
        child2.extend(crossoverParent2[:crossoverPoint])
        child2.extend(crossoverParent1[crossoverPoint:])

        population.append(child1)
        population.append(child2)

    return population


def mutation(population, mutationCount):
    chromosomeLenght = len(population[0])
    for i in range(0, mutationCount):
        mutationParent = random.choice(population)

        mutationPoint = random.randint(0, chromosomeLenght-1)
        mutationGene = random.randint(0, chromosomeLenght-1)

        child = mutationParent
        child[mutationPoint] = mutationGene

        population.append(child)

    return population


