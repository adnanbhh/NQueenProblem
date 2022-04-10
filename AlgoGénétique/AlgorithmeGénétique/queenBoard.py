import numpy as np

def CreateBoard(formation, sizeOfChromosome):
    board = []
    for row in range(0, sizeOfChromosome):
        array = []
        for column in range(0, sizeOfChromosome):
            if row == formation[column]:
                array.append("Q")
            else:
                array.append(".")
        board.append(array)

    print("La solution est")
    print(np.matrix(board))
