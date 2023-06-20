# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res, q = [], [root]

        while q:
            
            curLen = len(q)
            curLevel = []

            for i in range (curLen):
                node = q.pop(0)

                if node:
                    curLevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if curLevel:
                res.append(curLevel)
        
        return res
