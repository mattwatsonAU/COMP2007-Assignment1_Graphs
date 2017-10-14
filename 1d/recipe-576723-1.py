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
print(dictAdjList)



def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    print(type(node))
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
graph = {'A':['B','E','G'],'B':['E','C'],'C':['D'],'F':['G']}
print(type(graph))
# print(recursive_dfs(graph, 'B'))
# print(iterative_dfs(graph, 'A'))
print(iterative_bfs(graph, 'A'))
