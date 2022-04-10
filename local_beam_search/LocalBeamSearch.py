from heapq import heappush
from heapq import heappushpop


def local_beam_search(problem, k=5, limit=1000):
    global current
    front, seen = [], set()
    for i in range(k):
        current = problem.initial()
        front.append((problem.value(current), current))
    cnt = 0
    while front and cnt < limit:
        nextfront = []
        for val, node in front:
            neighbours = problem.children(node)
            for neighbour in neighbours:
                if neighbour not in seen:
                    seen.add(neighbour)
                    value = problem.value(neighbour)
                    # the number of attacks is value
                    if value == 0:
                    	#cnt is the number of iterations
                        print("local beam: %d" % cnt)  
                        return neighbour
                    if len(nextfront) < k:
                        heappush(nextfront, (value, neighbour))
                    else:
                        val, node = heappushpop(nextfront, (value, neighbour))
                        seen.remove(node)
        front = nextfront
        cnt += 1
    return current