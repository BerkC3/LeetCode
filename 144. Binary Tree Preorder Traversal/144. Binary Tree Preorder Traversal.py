# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, result, current = [], [], root
        while stack or current:
            if not current:
                current = stack.pop()
            while current:
                result.append(current.val)
                if current.right:
                    stack.append(current.right)
                current = current.left
        return result