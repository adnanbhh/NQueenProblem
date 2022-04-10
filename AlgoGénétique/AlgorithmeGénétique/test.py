from algorithm import  crossover, mutation, sortPopulation, countThreat, \
    initializePopulation
from queenBoard import  CreateBoard

sizeOfPopulation = 20 
sizeOfChromosome = 8
numberOfIterations = 1000
mutationCount = 5
crossoverCount = 5

population = initializePopulation(sizeOfPopulation, sizeOfChromosome)

for iteration in range(0, numberOfIterations ):
    population = crossover(population, crossoverCount)
    population = mutation(population, mutationCount)
    population = sortPopulation(population)
    population = population[:sizeOfPopulation]

CreateBoard(population[0], sizeOfChromosome)
print("Le chromosome obtenu est: " + str(population[0]))
print("Le nombre des attaques: " + str(countThreat(population[0])))




