graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

#key = graph.keys()
#print(key)
#print(graph["A"])
def BFS(graph,s):
    queue = []
    seen = set()
    seen.add(s)
    parent = {s : None}
    queue.append(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
#        print(vertex)
    return parent
    
startpos = "E"    
parent = BFS(graph,startpos)

#for key in parent:
#    print(key,parent[key])

tagpos = "B"
while tagpos != None:
    print(tagpos)
    tagpos = parent[tagpos]