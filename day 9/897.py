# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def find(p):
            if p:
                find(p.left)
                self.res.append(p.val)
                find(p.right)

        self.res = []
        find(root)

        new_root = TreeNode(self.res[0])
        res_root = new_root

        for i in range(1, len(self.res)):
            new_root.right = TreeNode(self.res[i])
            new_root = new_root.right

        return res_root