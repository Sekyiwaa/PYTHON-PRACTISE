def topological_sort(input):
    """
    :type input: Dict[str, List[int]]
    :rtype: List[int]
    """
    
    graph = {int(k): v for k, v in input.items()}
    
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of each vertex to 0
    
    # Initialize in-degree of each vertex
    for u in graph:
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1
    
    # Create a queue to store the vertices with in-degree 0
    queue = [u for u in in_degree if in_degree[u] == 0]
    
    # Create a list to store the sorted vertices
    sorted_vertices = []
    
    # Perform topological sort
    while queue:
        u = queue.pop(0)
        sorted_vertices.append(u)
        
        # Decrease the in-degree of adjacent vertices
        for v in graph.get(u, []):
            in_degree[v] -= 1
            
            # If the in-degree becomes 0, add it to the queue
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check if there is a cycle in the graph
    if len(sorted_vertices) != len(in_degree):
        raise ValueError("The graph contains a cycle.")
    
    return sorted_vertices