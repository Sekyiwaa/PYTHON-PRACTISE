def is_bipartite(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    colors = {}
    
    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - color):
                return False
        return True

    for node in graph:
        if node not in colors:
            if not dfs(node, 0):
                return False
                
    return True