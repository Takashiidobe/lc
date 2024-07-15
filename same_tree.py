from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        We can recursively define the same tree as follows:
        1. if the two tree nodes are null
        2. if the two tree nodes are non-null and they have the same value.
        We then apply the same rule to all nodes in both trees.
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# @leet end


def test():
    assert 2 + 2 == 4
