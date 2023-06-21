"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNew = {}

        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            else:
                copy = Node(node.val)
                oldNew[node] = copy
                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
                return copy
        
        if node:
            return dfs(node)
        else:
            return None
