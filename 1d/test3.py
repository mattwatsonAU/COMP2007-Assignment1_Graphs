def Graph():
    graph={}
    size1=int(input('Enter the size of the graph:'))
 
    for i in range(size1):
        node=(input('Enter a node:'))
        adj=[]
        ad=(input('Enter adjacent vertex:( enter -1 when done):'))
        while(ad!='-1'):
            adj.append(ad)
            ad=(input('Enter adjacent vertex:( enter -1 when done)'))
        graph[node]=adj
 
    visited={}
    for i in graph.keys():
        visited[i]=False
    print(visited)
    start=input('Enter start vertex:')
    end=input('Enter start vertex:')
    print(graph)
    print(find_path(graph,start,end))
 
def find_path(graph,start,end, path=[]) :
    path=path+[start]
    if start==end :
        return path
    if start not in graph:
        return None
    else :
        for node in graph[start] :
                 if node not in path:
                    newpath = find_path(graph, node, end, path)
                 if newpath :
                    return newpath
        return None
 
def main() :
    Graph()
 
if __name__=='__main__' :
    main()