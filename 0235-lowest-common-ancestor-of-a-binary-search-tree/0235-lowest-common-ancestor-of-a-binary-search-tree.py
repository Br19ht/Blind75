# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr = root

        if root.val > p.val and root.val > q.val:
            #only left tree

            curr = root.left
            return self.lowestCommonAncestor(curr, p, q)
            
        elif root.val < p.val and root.val < q.val:
            #only right tree

            curr = root.right
            return self.lowestCommonAncestor(curr, p, q)
            
        elif (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            #in-between

            return curr

        elif root.val == p.val:
            return p
        
        elif root.val == q.val:
            return q