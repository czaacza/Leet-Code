class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for edge in edges:
            self.addEdge(edge)
        

    def addEdge(self, edge: List[int]) -> None:
        frm, to, cost = edge
        self.graph[frm].append((cost, to))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()

        while heap:
            curr_cost, curr_node = heapq.heappop(heap)
            visited.add(curr_node)

            if curr_node == node2:
                return curr_cost

            for n_cost, n_node in self.graph[curr_node]:
                if n_node not in visited:
                    heapq.heappush(heap, (curr_cost + n_cost, n_node))


        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)