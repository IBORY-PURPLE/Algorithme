# for v in graph: heapq.heappush(pq, (D[v], v))

graph = {
    's' : {'t':10, 'y':5},
    't' : {'x':1, 'y':2},
    'y' : {'t':3, 'x':9, 'z':2},
    'x' : {'z':4},
    'z' : {'s':7, 'x':6}
}