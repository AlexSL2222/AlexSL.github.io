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

def DFS(graph,s):
    stack = []
    seen = set()
    seen.add(s)
    stack.append(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)
DFS(graph,"A")