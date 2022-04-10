from LocalBeamSearch import local_beam_search
from Queen import NQueensSearch

# create and show the board thaat simulat our solution
def printBoard(result):
    board = []
    for col in result:
        line = ['.'] * 8
        line[col] = 'Q'
        board.append(str().join(line))
    charlist = list(map(list, board))
    for line in charlist:
        print(" ".join(line))


class TestLocalSearch():
    def testLocalSearch(self, problem, local_search):
        cnt = 0
        for i in range(10):
            result = local_search(problem)
            if problem.value(result) == 0:
                print(result)
                printBoard(result)
                cnt += 1



if __name__ == "__main__":
    test = TestLocalSearch()
    print("local beam search")
    test.testLocalSearch(NQueensSearch(),local_beam_search)
