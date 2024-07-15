from typing import Optional
from utils import TreeNode


# @leet start
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        To invert a binary tree, we want to change every left and right subtree.
        To do this, we swap them and then iterate through the left and right sutbrees of the root.
        This is easiest done recursively.
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# @leet end


def test():
    assert 2 + 2 == 4
