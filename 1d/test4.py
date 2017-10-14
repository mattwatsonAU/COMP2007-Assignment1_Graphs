from collections import deque

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        # print(type(g))
        enqueued |= new
        queue.extend([(n, child) for child in new])

def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None # or raise appropriate exception

def shortest_path_num(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None # or raise appropriate exception


if __name__ == '__main__':
    # a sample graph
    graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F', 'D'],
             'F': ['C']}
    # print(type(graph))
    numgraph = {'0': ['1', '5','7'],
                '1': ['0','5'],
                '2': ['3'],
                '3': ['2','4'],
                '4': ['3'],
                '5': ['1'],
                '6': ['7'],
                '7': ['0','6']}
    # print(type(numgraph))

    n = int(input())
    m = int(input())


    edges, queries = [], []

    for _ in range(m):
        edges.append(input().split())

    dictAdjList = {}

    dictAdjList = {k: [] for k in range(n)}


    for x in edges:
        u = int(x.pop(0))
        # print("U: ",u)
        v = int(x.pop(0))
        dictAdjList[u].append(v)
        dictAdjList[v].append(u)
    # print("Adjacency list:")
    # print(dictAdjList)
    # print(graph)
    # print(numgraph)

    # print(shortest_path(graph, 'A', 'D'))
    # print(shortest_path_num(numgraph, '2', '5'))
    shortest_path(graph, 'A', 'D')
    shortest_path_num(numgraph, '2', '5')