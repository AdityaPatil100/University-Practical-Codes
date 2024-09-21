class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        visited = set()
        queue = [start]
        queue_start = 0

        while queue_start < len(queue):
            vertex = queue[queue_start]
            queue_start += 1

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                neighbors = self.graph.get(vertex, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Accepting input from the user
if __name__ == "__main__":
    g = Graph()

    # Get the number of edges and vertices from the user
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Get the edges from the user
    print("Enter the edges in the format (source, destination):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    # Get the starting vertex from the user
    start_vertex = int(input("Enter the starting vertex: "))

    # Perform BFS traversal
    print("Breadth-First Traversal (starting from vertex", start_vertex, "):")
    g.bfs(start_vertex)
