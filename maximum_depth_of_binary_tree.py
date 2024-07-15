from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        """
        To find the maximum depth of a tree, we can divide it into subproblems.
        1. If the root is null, the depth is 0.
        2. If the root is non-null, the depth is the maximum of the left and right
        sutbrees + 1.
        We apply that rule throughout the tree to get the depth.
        """
        if not root:
            return depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @leet end


def test():
    assert 2 + 2 == 4
