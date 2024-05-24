import heapq

class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_connection(self, user1, user2, weight=1):
        if user1 not in self.graph: self.graph[user1] = []
        if user2 not in self.graph: self.graph[user2] = []
        self.graph[user1].append((user2, weight))
        self.graph[user2].append((user1, weight))

    def find_shortest_path(self, start, end):
        """Implementation of Dijkstra's Algorithm for Network Routing"""
        queue = [(0, start, [])]
        seen = set()
        while queue:
            (cost, node, path) = heapq.heappop(queue)
            if node not in seen:
                seen.add(node)
                path = path + [node]
                if node == end: return path
                for (next_node, weight) in self.graph.get(node, []):
                    heapq.heappush(queue, (cost + weight, next_node, path))
        return None

# Example Usage for Software Engineering Portfolio
network = SocialGraph()
connections = [('User_A', 'User_B'), ('User_B', 'User_C'), ('User_A', 'User_C')]
for u1, u2 in connections:
    network.add_connection(u1, u2)

print(f"Optimal Routing Path: {network.find_shortest_path('User_A', 'User_C')}")
