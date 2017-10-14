parent = dict()
rank = dict()

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edgesin = []
for _ in range(m):
    edgesin.append(input().split())

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

for _ in range(n_A):
	A.append(input().split())

#Initialise an empty graph
graph={
			'vertices': list(range(n)),
			'edges': set([]),
		}

#Fill it with our edges in a a new order, weight(in), u, v
for x in edgesin:
	u = int(x.pop(0))
	v = int(x.pop(0))
	weightin = float(x.pop(0))
	lookup = ([str(u),str(v)])
	
	#The following two if statements check if the edge being added is a mandatory edge and if so, makes its
	if lookup in A:
		weightin = weightin*-1
	
	rev_lookup = ([str(v),str(u)])
	if rev_lookup in A:
		weightin = weightin*-1
			
	graph['edges'].update([(weightin, u, v)])

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
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

def algorithm(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    MST = set()
    
    totalweight = 0

    edges = list(graph['edges'])

    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            totalweight+=abs(weight)
            MST.add(edge)
    
    totalweight = "%.2f" % totalweight
    return totalweight


print(algorithm(graph))