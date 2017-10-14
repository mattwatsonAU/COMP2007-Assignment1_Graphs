# line = input()
# # n, m = map(int, line.split())
# print(line)

# print(n,m)

# for _ in range(n):
#   line = input()
#   x, y, z = map(float, line.split())
#   print(x, y)

n = int(input())
m = int(input())

#print(n)
#print(m)

edges, queries = [], []

for _ in range(m):
    edges.append(input().split())

# print(edges)

# for line in edges:
#         Type = line.split(" ")
#         x = Type[1]
#         y = Type[2]
#         print(x,y)


for element in edges:
    print(element[1])

q = int(input())

#print(q)

for _ in range(q):
    queries.append(input().split())

# print(queries)

# for _ in queries:
#     print(int(True))