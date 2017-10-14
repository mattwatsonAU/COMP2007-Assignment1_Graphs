# list_ = open("graph1000.in").read().split()

# value1 = list_[5]
# print(value1)

# with open('graph1000.in') as f:
#     lines = f.readlines()

# lines = [line.rstrip('\n') for line in open('graph1000.in')]

# for elem in list_:
#         print(elem)

f=open('graph8.in')
lines=f.readlines()


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set([])}

# print(graph)
#DFS
def dfs(graph, start):
    visited, stack = set(), [start]
    # print(visited)
    # print(stack)
    while stack:
        # print(stack)
        vertex = stack.pop()
        # print(vertex)
        # print(stack)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] -     visited)
    return visited

dfs_results = dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
# print(dfs_results)

def dfs_paths(graph, u, v):
    stack = [(u, [u])]
    print(stack)
    while stack:
        (vertex, path) = stack.pop()
        print(type(vertex))
        print(type(path))
        for next in graph[vertex] - set(path):
            if next == v:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# resultsAG = list(dfs_paths(graph, 'A', 'G')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
resultsAF = list(dfs_paths(graph, 'A', 'F'))

# if resultsAG == []:
# 	print("AG has no paths")
# else: print("AG has a path")

if resultsAF == []:
	print("AF has no paths")
else: print("AF has a path")
