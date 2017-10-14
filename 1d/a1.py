from collections import deque

n = int(input())
m = int(input())

edges, queries = [], []

for _ in range(m):
    edges.append(input().split())

#create an empty dict to hold our Graph Adjacency List
dictAdjList = {}

#initialise the dict with lists which will eventually be filled with corresponding edges
dictAdjList = {k: [] for k in range(n)}

#parse into an adjacency list
for x in edges:
	u = int(x.pop(0))
	v = int(x.pop(0))
	dictAdjList[u].append(v)
	dictAdjList[v].append(u)

q = int(input())

for _ in range(q):
    queries.append(input().split())

def bfs(graph, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        #need to cast n from a string to an int otherwise we get a key error
        new = set(graph[int(n)]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

def check_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                if child==None:
                	break
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return 1 # yes, there is a path in G between u and v
    return 0 # no, there is no path connecting u and v in G

for _ in queries:
	#set start as the first value
	start = _[0]
	#set end as the second value 
	end = _[1]
	print(check_path(dictAdjList, int(start), int(end)))