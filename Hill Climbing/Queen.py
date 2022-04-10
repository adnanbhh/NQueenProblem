from random import choice
from collections import defaultdict
from collections import Counter
from random import randrange
class NQueensSearch():

    #fixe the board size in 8, if we want to change it after its gonna be easier
    def __init__(self):
        self.N = 8

    #initialisation
    def initial(self):
        return tuple(randrange(self.N) for i in range(self.N))

    # this fct will return true if we have achive our goal, that none queen will attack none other queen
    def goal_test(self, state):
        x, y, z = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in x or row - col in y or row + col in z:
                return False
            x.add(col)
            y.add(row - col)
            z.add(row + col)
        return True

    # the number of queens that attack eaach others
    def value(self, state):
        x, y, z = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            x[col] += 1
            y[row - col] += 1
            z[row + col] += 1
        clashes = 0
        for cnt in [x, y, z]:
            for key in cnt:
                clashes += cnt[key] * (cnt[key] - 1) // 2
        return -clashes

    #child
    def children(self, state):
        children = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    child = list(state)
                    child[row] = col
                    children.append(tuple(child))
        return children
    #generate a child
    def random_child(self, state):
        row = randrange(self.N)
        col = randrange(self.N - 1)
        if col >= state[row]:
            col += 1
        child = list(state)
        child[row] = col
        return tuple(child)
