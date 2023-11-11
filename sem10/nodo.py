from collections import deque
def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False:
                nodes[b].visited = True
                print(b)
                q.append(b)
class Node():
    def __init__(self):
        self.visited = False
    #resto de atributos
    #Se definen las aristas
    e = dict()
    e['A'] = set(['C', 'H'])
    e['C'] = set(['A', 'F', 'H', 'S'])
    e['F'] = set(['C', 'S'])
    e['H'] = set(['A', 'C', 'S'])
    e['S'] = set(['H', 'C', 'F'])
    #se definen los nodos
    v = dict()
    for k in e.keys():
        v[k] = Node()
        BFS(v, e, 'A')