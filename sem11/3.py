from collections import deque
 
def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    
    size = 1
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].visited = True
                q.append(b)
                size += 1
    return size
 
def contGrafos(nodes, edges):
    numGrafos = 0
    maxSize = 0
 
    for node in nodes:
        if nodes[node].visited == False:
            size = BFS(nodes, edges, node)
            maxSize = max(maxSize, size)
            numGrafos += 1
 
    return [numGrafos, maxSize]
 
class Node():
    def _init_(self):
        self.visited = False
        self.distance = 0
 
for i in range(int(input())):
    e = dict()
    R = int(input())
    for j in range(R):
        a, b = map(int, input().split())
        if a not in e.keys(): 
            e[a] = set()
        e[a].add(b)
        if b not in e.keys():
            e[b] = set()
        e[b].add(a)
    
    v = dict()
    for k in e.keys():
        v[k] = Node()
    
    for j in contGrafos(v,e): print(j, end = " ")
    print()