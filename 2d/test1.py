parent = dict()
rank = dict()

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edgesin = []
for _ in range(m):
    edgesin.append(input().split())

# print(edgesin)

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []


for _ in range(n_A):
	A.append(input().split())
# print(n_A, A)
	
mst_weight = 0.

# Print the weight of the mst to two decimal-places. 
# print('{:.2f}'.format(mst_weight))






graphin={
			'vertices': list(range(n)),
			'edges': set([]),
		}

#Fill it with our edges in a a new order, weight(in), u, v
for x in edgesin:
	u = int(x.pop(0))
	v = int(x.pop(0))
	weightin = float(x.pop(0))
	# dictAdjList[u].append(v)
	# dictAdjList[v].append(u)
	lookup = ([str(u),str(v)])
	# print(lookup)
	if lookup in A:
		# print("Its a me, MARIO")
		weightin = weightin*-1
		# print(weightin)
	
	rev_lookup = ([str(v),str(u)])
	# print(lookup)
	if rev_lookup in A:
		# print("Its a me, MARIO")
		weightin = weightin*-1
		# print(weightin)
		

	graphin['edges'].update([(weightin, u, v)])
	
# print(graphin['edges'])
# print(graphin)
# print("Edges In type: ", type(graphin['edges']))

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    # print("Parent: ",parent[vertice])
    if parent[vertice] != vertice:
    	parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        # print(vertice)



    minimum_spanning_tree = set()
    # minimum_spanning_tree = set([
    #         (3, 0, 3),
    #         (4, 1, 2),
    #         ])
    
    totalweight = 0
    # print(minimum_spanning_tree)
    # print(edges)
    edges = list(graph['edges'])
    # print("Edges type: ", type(graph['edges']))
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        # print(edge)
        # print("Edge: ",edge)
        # print(weight, vertice1, vertice2)
        # print(vertice1, vertice2)
        # print("Find vertices 1 and 2: ",find(vertice2),find(vertice2))
        # print("still here")
        # print(find(vertice1) != find(vertice2))
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            # print ("match")
            # print("Vertice1: ",vertice1,"Vertice2: ",vertice2)
            # print("Tree before append: ",minimum_spanning_tree)
            totalweight+=abs(weight)
            minimum_spanning_tree.add(edge)
            # print("Tree after append: ",minimum_spanning_tree)
            # print(type(minimum_spanning_tree))
    # return minimum_spanning_tree
    totalweight = "%.2f" % totalweight
    return totalweight

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }

numgraph = {
			'vertices': [0, 1, 2, 3, 4, 5],
			'edges': set([
				(1, 0, 1),
				(5, 0, 2),
				(0, 0, 3),
				(0, 1, 2),
				(2, 1, 3),
				(1, 2, 3),
				])
		}

numgraph8 = {
			'vertices': [0, 1, 2, 3, 4, 5, 6, 7],
			'edges': set([
				(0.732, 0, 1),
				(0.134, 0, 3),
				(0.112, 0, 4),
				(0.770, 1, 4),
				(0.379, 2, 5),
				(0.984, 2, 6),
				(0.577, 2, 7),
				(0.642, 3, 4),
				(0.763, 3, 6),
				(0.589, 3, 7),
				(0.473, 4, 5),
				(0.334, 4, 7),
				(0.748, 5, 6),
				(0.544, 5, 7),
				(0.474, 6, 7),
				])
		}

numgraph8_forced = {
			'vertices': [0, 1, 2, 3, 4, 5, 6, 7],
			'edges': set([
				(-0.732, 0, 1),
				(0.134, 0, 3),
				(0.112, 0, 4),
				(0.770, 1, 4),
				(-0.379, 2, 5),
				(-0.984, 2, 6),
				(0.577, 2, 7),
				(0.642, 3, 4),
				(-0.763, 3, 6),
				(0.589, 3, 7),
				(0.473, 4, 5),
				(0.334, 4, 7),
				(0.748, 5, 6),
				(0.544, 5, 7),
				(0.474, 6, 7),
				])
		}

minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
# assert kruskal(graph) == minimum_spanning_tree
# print(kruskal(numgraph))
# print(kruskal(numgraph8))
# print(kruskal(numgraph8_forced))
print(kruskal(graphin))
# print(numgraph8)
# print(graphin)