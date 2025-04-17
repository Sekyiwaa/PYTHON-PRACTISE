from collections import defaultdict, deque

def longest_path(graph):
    def topological_sort(graph, all_nodes):
        in_degree = {node: 0 for node in all_nodes}
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        zero_in_degree_queue = deque([u for u in in_degree if in_degree[u] == 0])
        topo_order = []

        while zero_in_degree_queue:
            u = zero_in_degree_queue.popleft()
            topo_order.append(u)
            for v in graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    zero_in_degree_queue.append(v)

        return topo_order

    if not graph:
        return 0
        
    graph = graph["graph"]
    all_nodes = set(graph.keys())
    
    for edges in graph.values():
        all_nodes.update(edges)

    longest_paths = {node: 0 for node in all_nodes}

    topo_order = topological_sort(graph, all_nodes)

    for node in topo_order:
        if node in graph:
            for child in graph[node]:
                longest_paths[child] = max(longest_paths[child], longest_paths[node] + 1)

    return max(longest_paths.values(), default=0)