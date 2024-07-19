from typing import Optional
from utils import TreeNode
from itertools import islice


# @leet start
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        We want to return the kth smallest element in a BST.
        To do this, we can traverse the entire BST in order, and then stop at
        the kth smallest element.
        Since we traverse in order, we need to just see those k elements.

        This solution does that, but turns it into an iterator, and then seeks to
        the kth - 1 element and then returns that element.
        """

        def traverse(node):
            if node:
                yield from traverse(node.left)
                yield node.val
                yield from traverse(node.right)

        return next(islice(traverse(root), k - 1, None))


# @leet end


def test():
    assert 2 + 2 == 4
