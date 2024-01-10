# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {}

        def create_graph(node):
            nonlocal graph
            if node is None:
                return None

            left_node = create_graph(node.left)
            right_node = create_graph(node.right)

            if node.val not in graph:
                graph[node.val] = []

            if left_node is not None:
                if left_node.val not in graph:
                    graph[left_node.val] = []

                graph[node.val].append(left_node.val)
                graph[left_node.val].append(node.val)

            if right_node is not None:
                if right_node.val not in graph:
                    graph[right_node.val] = []

                graph[node.val].append(right_node.val)
                graph[right_node.val].append(node.val)

            return node
        
        def bfs(graph):
            queue = deque([(start, 0)])
            visited = set()
            max_dist = 0

            while queue:
                cur, cur_dist = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)

                for n in graph[cur]:
                    queue.append((n, cur_dist+1))
                
                max_dist = max(max_dist, cur_dist)
            
            return max_dist


        create_graph(root)
        return bfs(graph)          



            


        