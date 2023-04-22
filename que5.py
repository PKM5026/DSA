def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
# Example usage
graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: []}

if has_cycle(graph):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")