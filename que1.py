from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex, end=' ')
            
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Perform a BFS traversal of the graph starting from vertex 'A'
start = 'A'
bfs(graph, start)
